import simple_draw as sd


def smile(point):
    x = point.x
    y = point.y
    face = sd.get_point(point.x, point.y)
    radius_face = 50
    eye_f = sd.get_point(-20 + x, 20 + y)
    eye = sd.get_point(20 + x, 20 + y)
    radius_eye = 10
    width = 2
    start_point_line = sd.get_point(-20 + x, -20 + y)
    end_point_line = sd.get_point(20 + x, -20 + y)
    color = sd.COLOR_YELLOW
    sd.circle(center_position=face, radius=radius_face, color=color, width=width)
    sd.circle(center_position=eye_f, radius=radius_eye, color=color, width=width)
    sd.circle(center_position=eye, radius=radius_eye, color=color, width=width)
    sd.line(start_point=start_point_line, end_point=end_point_line, color=color, width=width)
