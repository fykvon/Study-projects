import simple_draw as sd

sd.resolution = (1400, 950)


def house():
    housewall()
    window()
    triangle(point1, angle=3, length=300)


def housewall():
    for row, y in enumerate(range(0, 350, 10)):
        start = 10 if row % 2 else 0
        for x in range(1000, 1300, 30):
            start = sd.get_point(x, y)
            end = sd.get_point(x + 30, y + 10)
            sd.rectangle(right_top=end, left_bottom=start, color=sd.COLOR_ORANGE, width=1)


def window():
    sd.rectangle(left_bottom=sd.get_point(1080, 150), right_top=sd.get_point(1220, 300), color=sd.background_color)


def figures(point, angle_quantity, angle, length):
    step = round(360 / angle_quantity)
    final_angle = 360 - step
    for step in range(angle, final_angle, step):
        point = sd.vector(start=point, angle=step, length=length, width=3)
    sd.line(start_point=point1, end_point=point, width=3)


def triangle(point1, angle, length):
    figures(point=point1, angle_quantity=3, angle=angle, length=length)


point1 = sd.get_point(1000, 350)
