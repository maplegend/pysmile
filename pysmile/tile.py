import pygame
from abc import ABC
from .renderer import Renderer


class Tile(Renderer, ABC):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 0, 0, 0)
