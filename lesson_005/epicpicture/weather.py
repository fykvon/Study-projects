import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


# def weather():
#     rainbow()
#     snow()

def rainbow():
    point = sd.get_point(0, 0)
    radius = 1400
    for color in rainbow_colors[::-1]:
        radius += 11
        sd.circle(point, radius=radius, color=color, width=10)


def snow():
    snowfall = []
    for i in range(20):
        snowfall.append([sd.random_number(0, 200), sd.random_number(600, 1200), sd.random_number(10, 30)])
    while True:
        sd.start_drawing()
        for index, (x, y, length) in enumerate(snowfall):
            point = sd.get_point(x, y)
            sd.snowflake(center=point, color=sd.background_color, length=length)
            snowfall[index][1] -= sd.random_number(5, 50)
            new_point = sd.get_point(x, snowfall[index][1])
            sd.snowflake(center=new_point, color=sd.COLOR_WHITE, length=length)
            if length > y:
                snowfall[index][1] = sd.random_number(600, 1200)
                sd.snowflake(center=new_point, color=sd.background_color, length=length)

        sd.finish_drawing()
        sd.sleep(0.1)

        if sd.user_want_exit():
            break


root_point = sd.get_point(550, 30)


def sun():
    sd.circle(center_position=sd.get_point(1000, 700), radius=50, color=sd.COLOR_YELLOW, width=0)
    # sd.snowflake(center=sd.get_point(1000,700), length=120, color=sd.COLOR_YELLOW,factor_a=0.000001,factor_b=0.0001)
    for angle in range(0, 360, 10):
        sd.vector(start=sd.get_point(1000, 700), angle=angle, length=120, width=1)
