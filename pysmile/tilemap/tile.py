import pygame


class Tile:
    def __init__(self, texture, name, meta={}, rect=pygame.Rect(0, 0, 0, 0)):
        self.rect = rect
        self.name = name
        self.texture = texture
        self.meta = meta
