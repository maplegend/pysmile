from math import pi, cos, sin


def gen_circle_points(pos, start, length, r, segments):
    def get_point(fun, x, p):
        return p + fun(2 * pi / segments * x + start) * r

    return [(get_point(cos, x, pos[0]), get_point(sin, x, pos[1])) for x in range(0, length)]


def gen_circle_segment(pos, start, length, r):
    points = gen_circle_points(pos, start, length, r, 360)
    res = []
    for x in range((length - 1) * 3):
        if x % 3 == 0:
            res.append(points[x // 3])
        elif (x - 1) % 3 == 0:
            res.append(points[x // 3 + 1])
        elif (x - 2) % 3 == 0:
            res.append(pos)
    return res
