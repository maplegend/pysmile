import pygame
from ..component import Component


class RendererComponent(Component):
    def __init__(self, renderer, size, shader=None):
        """
        :param renderer: renderer that will be used to render entity
        :param size: entity's size that will be displayed
        :param shader: shader that will be applied on entity
        """
        super().__init__()
        self.renderer = renderer
        self.size = size
        self.shader = shader

    def render(self, rect, ent):
        self.renderer.render(ent, rect)
