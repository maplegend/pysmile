import pygame
import random
from pysmile.game import Game
from pysmile.entity import Entity
from pysmile.components.renderer import RendererComponent
from pysmile.components.transform import TransformComponent
from pysmile.components.exit_on_escape import ExitOnEscape
from pysmile.renderers.rect_renderer import RectRenderer
from pysmile.renderers.text import TextRenderer
from pysmile.components.pygame_renderer import PyGameRendererComponent
from pysmile.math.vector2 import Vector2
from pysmile.colors import Colors
from pysmile.gl.shader import Shader
from pysmile.components.collisions.mouse import MouseColliderComponent
from pysmile.components.collisions.box_collider import BoxCollider
from pysmile.components.gui.button import ButtonComponent
from pysmile.events.button_press import ButtonPressEvent


class SimpleMenu:
    @staticmethod
    def start():
        pygame.init()
        size = width, height = (640, 480)
        game = Game()
        game.setup_default_components(size)
        scene = game.scene

        background = Entity()
        scene.add_entity(background)
        background.add_component(TransformComponent(Vector2(0, 0)))
        background.add_component(RendererComponent(RectRenderer(Colors.from_hex("#4C5B5C")), size))

        menu_label = Entity()
        scene.add_entity(menu_label)
        menu_label.add_component(TransformComponent(Vector2(width/2-120, 40)))
        menu_label.add_component(PyGameRendererComponent(TextRenderer("Simple Menu", 40, Colors.white), (100, 100)))

        click_label = Entity()
        scene.add_entity(click_label)
        click_label.add_component(TransformComponent(Vector2(width / 2 - 60, 90)))
        click_label_text = TextRenderer("Click count: 0", 20, Colors.white)
        click_label.add_component(PyGameRendererComponent(click_label_text, (100, 100)))

        play_button = Entity()
        scene.add_entity(play_button)
        play_button.add_component(TransformComponent(Vector2(width/2-100, 150)))
        shader = Shader.init_from_files("assets/button_shader.vert", "assets/button_shader.frag")
        play_button.add_component(RendererComponent(RectRenderer(Colors.from_hex("#4F6D7A")), (200, 50), shader))
        play_button.add_component(BoxCollider((200, 50)))
        play_button.add_component(MouseColliderComponent())
        play_button.add_component(ButtonComponent(shader, text="Play",
                                                  hover_color=Colors.from_hex("#3891A6"),
                                                  click_color=Colors.from_hex("#FDE74C")))

        exit_button = Entity()
        scene.add_entity(exit_button)
        exit_button.add_component(TransformComponent(Vector2(width/2-100, 250)))
        shader1 = Shader.init_from_files("assets/button_shader.vert", "assets/button_shader.frag")
        exit_button.add_component(RendererComponent(RectRenderer(Colors.from_hex("#9E3A35")), (200, 50), shader1))
        exit_button.add_component(BoxCollider((200, 50)))
        exit_button.add_component(MouseColliderComponent())
        exit_button.add_component(ButtonComponent(shader1, text="Exit",
                                                  hover_color=Colors.from_hex("#C24741"),
                                                  click_color=Colors.from_hex("#FDE74C")))

        def press(event):
            if event.entity == play_button:
                click_label_text.text = "Click count: {}".format(int(click_label_text.text.split(": ")[1])+1)
            elif event.entity == exit_button:
                game.exit()

        exit_button.event_manager.bind(ButtonPressEvent, press)

        game.add_component(ExitOnEscape())

        game.run()
