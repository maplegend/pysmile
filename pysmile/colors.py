import pygame


class ColorsObj:
    def __getattr__(self, attr):
        return pygame.color.THECOLORS[attr]


Colors = ColorsObj()

