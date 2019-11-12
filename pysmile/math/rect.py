import pygame
from .line_segment import LineSegment


class Rect(pygame.Rect):
    def __init__(self, x=0, y=0, w=0, h=0):
        if isinstance(x, tuple) and isinstance(y, tuple):
            super().__init__(x, y)
        else:
            super().__init__(x, y, w, h)

    @property
    def xy(self):
        return self.x, self.y

    @property
    def size(self):
        return self.width, self.height

    @property
    def corners(self):
        return [self.topright, self.bottomright, self.topleft, self.bottomleft]

    def intersect_line(self, line):
        if not self.collidepoint(*line.end.xy):
            return None
        for ed in self.edges:
            p = ed.intersection_point(line)
            if p is not None:
                return p
        return None

    @property
    def edges(self):
        return [
            LineSegment((self.x, self.y), (self.x+self.w, self.y)),
            LineSegment((self.x+self.w, self.y), (self.x + self.w, self.y + self.h)),
            LineSegment((self.x + self.w, self.y + self.h), (self.x, self.y+self.h)),
            LineSegment((self.x, self.y+self.h), (self.x, self.y)),
        ]

    def __hash__(self):
        return hash((self.x, self.y, self.w, self.h))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.w == other.w and self.h == other.h
