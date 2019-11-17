import pygame


class Color(tuple):
    def to_float(self):
        return tuple(ti / 255.0 for ti in self)


class ColorsObj:
    def from_rgb(self, r, g, b):
        return Color((r, g, b, 255))

    def from_hex(self, hex):
        hex = hex.lstrip('#')
        return Color(tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4)) + (255,))

    def __getattr__(self, attr):
        return Color(pygame.color.THECOLORS[attr])


Colors = ColorsObj()

