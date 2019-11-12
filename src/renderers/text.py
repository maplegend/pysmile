import pygame
from src.renderer import Renderer
from src.components.transform import TransformComponent
from src.colors import white, black


class TextRenderer(Renderer):
    def __init__(self, text, font_size=20, color=black, background_color=white):
        super().__init__()
        self.color = color
        self.background_color = background_color
        self.text = text
        self.font = pygame.font.Font(pygame.font.get_default_font(), font_size)

    def render(self, screen, entity):
        text = self.font.render(self.text, True, black, white)
        screen.fill(white)
        rect = entity.get_component(TransformComponent).rect
        screen.blit(text, (0, 0, rect.width, rect.height))
