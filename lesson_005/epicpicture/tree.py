import simple_draw as sd


def tree(start, angle, length):
    if length < 14:
        return
    v1 = sd.get_vector(start_point=start, angle=angle, length=length, width=1)
    v1.draw()
    random_length = sd.random_number(a=87, b=127) / 100
    next_length = length * .75 * random_length
    corner_random = sd.random_number(a=40 * 30, b=120 * 30) / 100
    next_point = v1.end_point
    next_angle = angle - corner_random
    next_angle_2 = angle + corner_random
    tree(start=next_point, angle=next_angle, length=next_length)
    tree(start=next_point, angle=next_angle_2, length=next_length)
