import pygame


class tuple(tuple):
    def to_float(self):
        return tuple(ti / 255.0 for ti in self)


class ColorsObj:
    def __getattr__(self, attr):
        return tuple(pygame.color.THECOLORS[attr])


Colors = ColorsObj()

