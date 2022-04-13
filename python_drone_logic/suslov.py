# -*- coding: utf-8 -*-

from astrobox.core import Drone
from robogame_engine.geometry import Point, Vector
from robogame_engine.theme import theme
from astrobox.themes.default import MOTHERSHIP_HEALING_DISTANCE


class SuslovDrone(Drone):
    list_drones = []
    role = None
    index = 0
    not_full_range, range, full_range = 0, 0, 0
    safe_zone = MOTHERSHIP_HEALING_DISTANCE

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_drones.append(self)

    def on_born(self):  # +
        self.index = self.list_drones.index(self)
        self.get_role()

    def on_stop_at_asteroid(self, asteroid):  # +
        if self.game_start():
            self.get_role()
        elif self.role == 'harvester' and self.target in self.asteroids:
            if self.payload + self.target.payload < 100 and self.get_nearest_asteroids(index=1):
                next_target = self.get_nearest_asteroids(index=1)
            else:
                next_target = self.mothership
            self.load_from(asteroid)
            self.turn_to(next_target)

    def on_stop_at_mothership(self, mothership):  # +
        if mothership == self.my_mothership:
            self.unload_to(mothership)
        else:
            self.load_from(mothership)
            self.turn_to(self.target)

    def on_load_complete(self):  # +
        if not self.is_full:
            if self.get_nearest_asteroids():
                self.target = self.get_nearest_asteroids()
            elif self.near_enemy_to_load():
                self.target = self.get_enemy(dead_drone=True)
        else:
            self.target = self.my_mothership
        self.move_at(self.target)

    def on_unload_complete(self):  # +
        if self.is_full:
            self.move_at(self.my_mothership)
        else:
            self.move_at(self.safety_position_near_base())

    def on_wake_up(self):
        if self.game_start():
            self.get_role()
        elif self.role == 'go_harvester':
            self.go_harvester()
        elif self.role == 'defender':
            self.defender()
        elif self.role == 'base_killer':
            self.base_killer()
        elif self.role == 'devastator':
            self.devastator()
        else:
            self.harvester()

    def game_start(self):
        return self.role == 'go_harvester'

    def on_heartbeat(self):
        self.check_drone_health()
        if self.role == 'harvester' and self.near_enemy_to_load():
            self.load_from(self.get_enemy(dead_drone=True))
        elif self.check_all_objects_is_empty():
            self.choose_target(self.my_mothership)

    def get_role(self, last_step=False, devastator_step=False):  # Распределение ролей
        if devastator_step:
            self.role = 'devastator'
        elif last_step:
            self.role = 'harvester'
        else:
            if self.role == 'go_harvester':
                self.go_harvester()
            elif self.shoot(target=self.get_enemies_mothership()):
                self.role = 'base_killer'
            else:
                self.role = 'defender'

    def go_harvester(self):
        self.choose_target(self.get_nearest_asteroids(index=self.index))

    def base_killer(self):  # логика уничтожителя базы
        if not self.near(self.safety_position_near_base()):
            self.move_at(self.safety_position_near_base())
        else:
            if self.get_enemies_mothership() and self.shoot(self.get_enemies_mothership()):
                self.target = self.get_enemies_mothership()
                self.shot_target()
            else:
                self.get_role()

    def defender(self):  # Логика дрона ащитника
        if not self.near(self.safety_position_near_base()):
            self.move_at(self.safety_position_near_base())
        else:
            self.target = self.get_enemy()
            self.shoot_enemy()
            if self.shoot(self.get_enemies_mothership()):
                self.get_role()
            elif not self.get_enemy():
                self.get_role(last_step=True)

    def devastator(self):  # Логика дрона атакуещего
        self.target = self.get_enemy(target=True)
        victim = self.target.my_mothership.coord if self.target and self.target.my_mothership.is_alive else None
        go_attack = self.safety_shot(one_enemy=True) and victim
        self.target = victim if go_attack else self.get_enemy(target=True)
        distance = self.gun.shot_distance if go_attack else self.safe_zone * 1.5
        start_point = victim if go_attack else None
        position = self.safety_position_near_base(distance=distance, start_point=start_point)
        if not self.target:
            self.get_role(last_step=True)
        elif not self.safety_shot():
            self.get_role()
        elif self.near(position):
            self.shot_target()
        else:
            self.move_at(position)

    def harvester(self):  # Логика сборщика
        if self.get_enemies_mothership():
            self.target = self.get_enemies_mothership()
            position = self.safety_position_near_base(start_point=self.target.coord, distance=self.gun.shot_distance)
            if self.near(position):
                self.shot_target()
            else:
                self.move_at(position)
        elif self.get_enemy(dead_drone=True):  # если есть убитый дрон, летим собирать с него руду
            self.choose_target(self.get_enemy(dead_drone=True))
        elif self.get_nearest_asteroids(index=len(self.harvesters())):  # Летим собирать руду с астероидов
            self.choose_target(self.get_nearest_asteroids(index=self.get_personal_asteroid_index()))
        elif self.get_nearest_asteroids():  # если есть астероид, летим собирать с него руду
            self.choose_target(self.get_nearest_asteroids())
        elif self.get_enemies_mothership(steal=True):  # Летим собирать руду с убитого вражеского корабля
            self.choose_target(self.get_enemies_mothership(steal=True))
        else:
            self.choose_target(self.my_mothership)

    def choose_target(self, target):
        self.target = target
        self.move_at(self.target)

    def safety_position_near_base(
            self, distance=safe_zone * 0.99, start_point=None, end_point=None, sweep=45):
        position = Circle(self.my_mothership, self.list_drones, self.index)
        return position.get_position_circle(distance, start_point, end_point, sweep)

    def get_enemies_mothership(self, destroy=True, steal=False):
        all_motherships = []
        for enemies_mothership in self.scene.motherships:  # Цикл определения какая из баз не моя
            if destroy and enemies_mothership != self.my_mothership and enemies_mothership.is_alive:  # Если живая
                all_motherships.append([enemies_mothership, self.distance_to(enemies_mothership)])
            elif steal and not enemies_mothership.is_alive and not enemies_mothership.is_empty:  # Если нет
                all_motherships.append([enemies_mothership, self.distance_to(enemies_mothership)])
        if all_motherships:
            all_motherships.sort(key=lambda x: x[1])
            return all_motherships[0][0]
        return None

    def get_enemy(self, number=0, target=False, dead_drone=False):
        enemies = []  # Создаю пустой список соперников и заполняю мёртвыми и живыми
        start_point = self.my_mothership if target else self
        for enemy in self.scene.drones:
            if enemy.team != self.team and enemy.is_alive:
                enemies.append((enemy, start_point.distance_to(enemy)))
            elif dead_drone and enemy.team != self.team and not enemy.is_alive and not enemy.is_empty:
                enemies.append((enemy, start_point.distance_to(enemy)))
        if number >= len(enemies):
            return None
        if enemies:  # сортируею что бы мёртвые враги оказались в конце
            enemies.sort(key=lambda x: x[1])
            return enemies[number][0]
        return None

    def safety_shot(self, one_enemy=False):
        enemies = []
        for enemy in self.scene.drones:
            if enemy.team != self.team and enemy.is_alive:
                enemies.append((enemy, self.my_mothership.distance_to(enemy)))
        if one_enemy:
            return len(enemies) == 1 and len(self.list_drones) >= 3
        return len(enemies) + 1 < len(self.list_drones)

    def shoot_enemy(self):
        n = 1
        while not self.shoot(target=self.target):
            if self.get_enemy(n):
                self.target = self.get_enemy(n)
                n += 1
            else:
                self.target = None
                break
        if self.shoot(self.target):
            self.shot_target()

    def shot_target(self):
        self.turn_to(self.target)
        self.gun.shot(self.target)

    def sufficient_distance(self, distance_points):
        return distance_points <= self.gun.shot_distance

    def shoot(self, target):
        if not target:
            return False
        return self.sufficient_distance(self.distance_to(target))

    def harvesters(self):
        n, drone_harvester = 0, {}
        for drone in self.list_drones:
            if drone.role == 'harvester':
                drone_harvester[drone.index] = n
                n += 1
        return drone_harvester

    def get_personal_asteroid_index(self):
        drone = self.harvesters()
        return drone[self.index]

    def check_drone_health(self, safe_share_of_health=0.6):  # + проверка хп.
        if self.health == 0 and self in self.list_drones:
            self.list_drones.remove(self)  # если дрон умер то убираем его из списка дронов
            for drone in self.list_drones:
                drone.index = self.list_drones.index(drone)
        elif 0 < self.health < theme.DRONE_MAX_SHIELD * safe_share_of_health:  # если жив то продолжает двигаться
            self.choose_target(self.my_mothership)

    def near_enemy_to_load(self):
        return self.get_enemy(dead_drone=True) and self.distance_to(self.get_enemy(dead_drone=True)) < 1

    def check_all_objects_is_empty(self):
        objects_empty = [
            self.get_nearest_asteroids() is None,
            self.get_enemies_mothership(steal=True) is None,
            self.get_enemy(dead_drone=True) is None
        ]
        return all(objects_empty)

    def get_nearest_asteroids(self, index=0, position=False):  # лижайший астероид
        distances_to_asteroids = {}
        for num, asteroid in enumerate(self.asteroids):
            distances_to_asteroids[asteroid] = self.distance_to(asteroid)
        distances_to_asteroids_sorted = sorted(distances_to_asteroids.items(), key=lambda item: item[1])
        if position:
            return distances_to_asteroids_sorted[index][0]
        fulls = [asteroid[0] for asteroid in distances_to_asteroids_sorted if asteroid[0].payload >= 100]
        not_empty = [asteroid[0] for asteroid in distances_to_asteroids_sorted if asteroid[0].payload > 0]
        if len(fulls) >= index + 1:
            return fulls[index]
        elif len(not_empty) >= index + 1:
            return not_empty[index]
        return None

    def move_at(self, target, speed=None):
        super().move_at(target=target, speed=speed)
        if 0 < self.payload < 100:
            self.not_full_range += self.distance_to(target)
        elif self.payload == 0:
            self.range += self.distance_to(target)
        else:
            self.full_range += self.distance_to(target)


class Circle:  # Класс по выбору места у базы
    positions = {}
    edges = []

    def __init__(self, my_mothership, list_drones, index):
        self.my_mothership = my_mothership
        self.list_drones = list_drones
        self.index = index

    def append_edges(self, amount_of_drones, sweep):
        amount_of_parts = amount_of_drones // 2
        edge_step = sweep // amount_of_parts
        index, from_ = 1, 0 if amount_of_drones % 2 != 0 else edge_step
        for _ in range(2):
            for i in range(from_, sweep + 1, edge_step):
                self.edges.append(i * index)
            index *= -1
            from_ = edge_step

    def find_position(self, vec_position, amount_of_drones, drone, sweep):
        if not self.edges:
            self.append_edges(amount_of_drones, sweep)
        final_vector = vec_position
        final_vector.rotate(self.edges[drone.index])
        return final_vector

    def find_new_positions_circle(self, start_point, end_point, distance, sweep):
        start_dot = start_point if start_point else self.my_mothership.coord
        end_dot = end_point if end_point else Point(theme.FIELD_WIDTH // 2, theme.FIELD_HEIGHT // 2)
        amount_of_drones = len(self.list_drones)
        vec = Vector.from_points(start_dot, end_dot)
        norm_vec = Vector(vec.x / vec.module, vec.y / vec.module)
        vec_position = Vector(norm_vec.x * distance, norm_vec.y * distance)
        for drone in self.list_drones:
            final_vector = self.find_position(vec_position, amount_of_drones, drone, sweep)
            final_point = (start_dot.x + final_vector.x, start_dot.y + final_vector.y)
            point = Point(final_point[0], final_point[1])
            self.positions[distance].append(point)
            vec_position.rotate(-self.edges[drone.index])

    def get_position_circle(self, distance, start_point, end_point, sweep):
        amount_of_drones = len(self.list_drones)
        if distance not in self.positions.keys() or len(self.positions[distance]) >= amount_of_drones:
            self.positions[distance], self.edges = [], []
            self.find_new_positions_circle(start_point, end_point, distance, sweep)
        return self.positions[distance][self.index]
