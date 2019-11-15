import pygame


class ColorsObj:
    def __getattr__(self, attr):
        print(attr)
        return pygame.color.THECOLORS[attr]


Colors = ColorsObj()

