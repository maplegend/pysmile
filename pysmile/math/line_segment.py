import pygame
from .vector2 import Vector2


class LineSegment:
    def __init__(self, start, end, x1=0, y1=0):
        """
        :param start: start point or x
        :param end: end point or y
        :param x1: none or x1
        :param y1: none or y1
        """
        if isinstance(start, pygame.Vector2) and isinstance(end, pygame.Vector2):
            self.start = start
            self.end = end
        elif isinstance(start, tuple) and isinstance(end, tuple):
            self.start = Vector2(start[0], start[1])
            self.end = Vector2(end[0], end[1])
        else:
            self.start = Vector2(start, end)
            self.end = Vector2(x1, y1)

    def vector(self):
        return self.end - self.start

    def equation(self):
        # Returns k and b from y = kx + b
        vec = self.vector()
        k = vec.y / (vec.x if vec.x != 0 else 0.000001)
        return k, self.start.y - self.start.x * k

    @property
    def is_vertical(self):
        return self.start.x == self.end.x

    @property
    def is_horizontal(self):
        return self.start.y == self.end.y

    def intersection_point(self, line, real=True):
        xdiff = (self.start.x - line.start.x, line.start.x - line.end.x)
        ydiff = (self.start.y - line.start.y, line.start.y - line.end.y)

        dxdiff = (self.start.x - self.end.x, xdiff[1])
        dydiff = (self.start.y - self.end.y, ydiff[1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        def lay_in_range(x, a, b):
            aa, ab = abs(a), abs(b)
            return min(aa, ab) <= abs(x) <= max(aa, ab)

        div = det(dxdiff, dydiff)
        if div == 0:
            # That needs refactoring
            if self.is_vertical and line.is_horizontal:
                if lay_in_range(self.start.x, line.start.x, line.end.x) \
                        and lay_in_range(line.start.y, self.start.y, self.end.y):
                    return Vector2(self.start.x, line.start.y)
                else:
                    return None
            if line.is_vertical and self.is_horizontal:
                if lay_in_range(line.start.x, self.start.x, self.end.x) \
                        and lay_in_range(self.start.y, line.start.y, line.end.y):
                    return Vector2(line.start.x, self.start.y)
                else:
                    return None

            return None

        t = det(xdiff, ydiff) / div
        x = self.start.x + t * (self.end.x - self.start.x)
        y = self.start.y + t * (self.end.y - self.start.y)

        if real:
            '''uxdiff = (dxdiff[0], xdiff[0])  # x1 - x2 | x1 - x3
            uydiff = (dydiff[0], ydiff[0])

            udxdiff = (uxdiff[0], xdiff[1])
            udydiff = (uydiff[0], ydiff[1])
            u = -det(uxdiff, uydiff) / det(udxdiff, udydiff)
            xt = line.start.x + u * (line.end.x - line.start.x)
            yt = line.start.y + u * (line.end.y - line.start.y)
            if 0 <= t <= 1 or 0 <= u <= 1:
                return None'''

            if not lay_in_range(x, self.start.x, self.end.x) or not lay_in_range(x, line.start.x, line.end.x):
                return None

        return Vector2(x, y)

    def __eq__(self, other):
        if not isinstance(other, LineSegment):
            return False
        return self.start == other.start and self.end == other.end

    def __str__(self):
        return "{} {} -> {} {}".format(*self.start.xy, *self.end.xy)


'''
    def intersection_point(self, line, real=True):
        """
        :param line: second line
        :param real: if true and point of intersection does not lay on both line segments method will return None
        :return: point of intersection
        """
        e = 0.001
        eq = self.equation()
        seq = line.equation()
        if -e <= eq[0] - seq[0] <= e:
            return None

        x = (seq[1] - eq[1]) / (eq[0] - seq[0])
        y = eq[0]*x + eq[1]
        if real:
            def lay_on_line(l):
                return min(l.start.x, l.end.x) <= x <= max(l.start.x, l.end.x) \
                          and min(l.start.y, l.end.y) <= y <= max(l.start.y, l.end.y)
            if not lay_on_line(self) or not lay_on_line(line):
                return None

        return Vector2(x, y)
'''
