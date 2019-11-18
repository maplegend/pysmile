from ..component import Component
from .transform import TransformComponent
from ..events.update import UpdateEvent
from pysmile.math.vector2 import Vector2
from .collisions.collider import Collider
from .renderer import RendererComponent
from pysmile.renderers.tile_renderer import TileRenderer
from .game.collision_handler import GameCollisionsHandlerComponent


class MoveComponent(Component):
    def __init__(self, acceleration, max_speed, normalize=True, flip=True, default_collision_check=True):
        """
        Init move component
        :param acceleration: how fast will be velocity increasing
        :param max_speed: maximum velocity
        :param normalize: normalize output vector i.e. move to all directions with same speed
        :param flip: flip texture when direction changed from left to right or vice versa
        """
        super().__init__()
        self.velocity = Vector2()
        self.direction = Vector2()
        self.acceleration = acceleration
        self.max_speed = max_speed
        self.entity = None
        self.normalize = normalize
        self.flip = flip
        self.default_collision_check = default_collision_check

    def set_direction(self, x, y):
        self.direction = Vector2(x, y)

    def add_direction(self, x, y):
        self.direction += Vector2(x, y)

    def update(self, event):
        if self.direction.magnitude() == 0:
            return

        trans = self.entity.get_component(TransformComponent)
        if not trans:
            return

        if self.normalize and self.direction.magnitude() != 0:
            self.direction.normalize_ip()

        if self.flip:
            rend = self.entity.get_component(RendererComponent)
            if isinstance(rend.renderer, TileRenderer):
                rend.renderer.flip = self.direction.x < 0

        if (self.velocity + self.direction*self.acceleration).magnitude() > self.max_speed:
            self.velocity = self.direction*self.max_speed
        else:
            self.velocity += self.direction * self.acceleration
        rect = self.entity.get_component(Collider).get_collider()[0]

        ch = self.entity.scene.game.get_component(GameCollisionsHandlerComponent)
        if ch is None or not self.default_collision_check:
            trans.position = trans.pos + self.velocity
            self.direction *= 0
            return

        move_x = False
        if not ch.check_rect_collision(rect.move(self.velocity.x, 0), [rect]):
            trans.position.x += self.velocity.x
            move_x = True

        if not ch.check_rect_collision(rect.move(self.velocity.x if move_x else 0, self.velocity.y), [rect]):
            trans.position.y += self.velocity.y

        self.direction *= 0

    def applied_on_entity(self, entity):
        self.entity = entity
        entity.event_manager.bind(UpdateEvent, self.update)
