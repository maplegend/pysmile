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
from pysmile.components.collisions.mouse import MouseColliderComponent
from pysmile.events.click import ClickEvent
from pysmile.events.hover import HoverEvent
from pysmile.components.animation import AnimationComponent
from pysmile.components.collisions.box_collider import BoxCollider


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
        shader.uniform_color = tuple(ti/255.0 for ti in Colors.red)
        shader.uniform_x_coord = 1.2
        play_button.add_component(RendererComponent(RectRenderer(Colors.white), (100, 100), shader))
        play_button.add_component(BoxCollider((100, 100)))
        play_button.add_component(MouseColliderComponent())

        def start_anim(_):
            if not play_button.contains_component(AnimationComponent):
                anim = AnimationComponent(step=-20, start=120, end=0,
                                          function=lambda x: shader.set_uniform("x_coord", x/100.0),
                                          completion=lambda: print("comp"))
                play_button.add_component(anim)
        play_button.event_manager.bind(HoverEvent, start_anim)

        exit_button = Entity()
        scene.add_entity(exit_button)
        exit_button.add_component(TransformComponent(Vector2(width/2-50, 150)))
        shader1 = Shader.init_from_files("assets/button_shader.vert", "assets/button_shader.frag")
        exit_button.add_component(RendererComponent(RectRenderer(Colors.white), (100, 100), shader1))

        game.add_component(ExitOnEscape())

        game.run()
