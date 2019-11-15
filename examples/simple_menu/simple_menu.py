import pygame
import random
from pysmile.game import Game
from pysmile.entity import Entity
from pysmile.components.renderer import RendererComponent
from pysmile.components.transform import TransformComponent
from pysmile.components.exit_on_escape import ExitOnEscape
from pysmile.renderers.rect_renderer import RectRenderer
from pysmile.math.vector2 import Vector2
from pysmile.colors import Colors
from pysmile.gl.shader import Shader


class SimpleMenu:
    @staticmethod
    def start():
        pygame.init()
        size = width, height = (640, 480)
        game = Game()
        game.setup_default_components(size)
        scene = game.scene

        play_button = Entity()
        scene.add_entity(play_button)
        play_button.add_component(TransformComponent(Vector2(width/2-50, 0)))
        shader = Shader.init_from_files("assets/button_shader.vert", "assets/button_shader.frag")
        shader.uniform_red = 1.0
        play_button.add_component(RendererComponent(RectRenderer(Colors.white), (100, 100), shader))

        exit_button = Entity()
        scene.add_entity(exit_button)
        exit_button.add_component(TransformComponent(Vector2(width/2-50, 150)))
        shader = Shader.init_from_files("assets/button_shader.vert", "assets/button_shader.frag")
        exit_button.add_component(RendererComponent(RectRenderer(Colors.white), (100, 100), shader))

        game.add_component(ExitOnEscape())

        game.run()
