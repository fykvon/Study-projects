# -*- coding: utf-8 -*-

# pip install -r requirements.txt

from astrobox.space_field import SpaceField
from suslov import SuslovDrone

if __name__ == '__main__':
    scene = SpaceField(
        speed=5,
        asteroids_count=11,
    )
    drones = [SuslovDrone() for _ in range(5)]
    scene.go()

# Второй этап: зачёт!
