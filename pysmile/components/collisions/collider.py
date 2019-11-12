from abc import abstractmethod
from pysmile.component import Component
from ..game.collision_handler import GameCollisionsHandlerComponent


class Collider(Component):

    def applied_on_entity(self, entity, static=False):
        ch = entity.scene.game.get_component(GameCollisionsHandlerComponent)
        if ch is None:
            return
        if static:
            ch.add_static_collider(self)
        else:
            ch.add_collider(self)

    @abstractmethod
    def get_collider(self):
        pass
