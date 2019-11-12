import pygame
from ..component import Component


class RendererComponent(Component):
    def __init__(self, renderer, size):
        super().__init__()
        self.renderer = renderer
        self.size = size

    def render(self, rect, ent):
        self.renderer.render(ent, rect)
