# PySmile
Component-based pygame wrapper

# Quick start
Install:

`pip install -e git+https://github.com/maplegend/pysmile.git#egg=pysmile`

Usage:

```python
import pygame
from pysmile.game import Game
from pysmile.entity import Entity
from pysmile.components.renderer import RendererComponent
from pysmile.components.transform import TransformComponent
from pysmile.components.exit_on_escape import ExitOnEscape
from pysmile.components.move import MoveComponent
from pysmile.components.key_control import KeyControlComponent
from pysmile.components.collisions.box_collider import BoxCollider
from pysmile.components.name import NameComponent
from pysmile.math.vector2 import Vector2
from pysmile.renderers.image_renderer import ImageRenderer


def main():
    #Initiate game
    pygame.init()
    size = (640, 480)
    game = Game()
    game.setup_default_components(size)
    scene = game.scene
    
    #Create player
    player = Entity()
    scene.add_entity(player)
    player.add_component(NameComponent("player"))

    key_bindings = [[pygame.K_a], [pygame.K_d], [pygame.K_w], [pygame.K_s]]

    player.add_component(MoveComponent(1, 2))
    player.add_component(KeyControlComponent(key_bindings))
    player.add_component(TransformComponent(Vector2(100, 100)))
    player.add_component(BoxCollider((16*2, 22*2), Vector2(0, 12)))
    player.add_component(RendererComponent(ImageRenderer("pygame.png"), (1000, 1000)))

    game.add_component(ExitOnEscape())
    
    #Start game
    game.run()


if __name__ == "__main__":
    main()

```
