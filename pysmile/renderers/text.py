import pygame
from pysmile.renderer import Renderer
from pysmile.colors import white, black


class TextRenderer(Renderer):
    def __init__(self, text, font_size=20, color=black, background_color=white):
        super().__init__()
        self.color = color
        self.background_color = background_color
        self.text = text
        self.old_text = ""
        self.font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        self.texture = None

    def render(self, entity, rect):
        return self.font.render(self.text, True, black, white)
