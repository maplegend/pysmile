import pygame
from pysmile.renderer import Renderer
from pysmile.colors import Colors


class TextRenderer(Renderer):
    def __init__(self, text, font_size=20, color=Colors.red, background_color=None, font=pygame.font.get_default_font()):
        super().__init__()
        self.color = color
        self.background_color = background_color
        self.text = text
        self.old_text = ""
        self.font = pygame.font.Font(font, font_size)
        self.texture = None

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)
        if key != "need_redraw":
            self.need_redraw = True

    def render(self, entity, rect):
        return self.font.render(self.text, True, self.color, self.background_color)
