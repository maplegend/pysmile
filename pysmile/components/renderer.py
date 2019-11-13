import pygame
from ..component import Component


class RendererComponent(Component):
    def __init__(self, renderer, size):
        """
        :param renderer: renderer that will be used to render entity
        :param size: entity's size that will be displayed
        """
        super().__init__()
        self.renderer = renderer
        self.size = size

    def render(self, rect, ent):
        self.renderer.render(ent, rect)
