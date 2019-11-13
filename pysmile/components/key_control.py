from ..component import Component
from .move import MoveComponent
from ..events.key_pressed import KeyPressedEvent


class KeyControlComponent(Component):
    def __init__(self, bindings):
        """
        Bind specified keys to move player through MoveComponent
        bindings: array of keys that needed to bind [left key, right key, up key, down key]
        """
        super().__init__()
        self.entity = None
        self.bindings = bindings

    def key_pressed(self, key_event):
        move = self.entity.get_component(MoveComponent)
        if move and len(self.bindings) >= 4:
            key = key_event.key
            if key in self.bindings[0]:
                move.add_direction(-1, 0)
            elif key in self.bindings[1]:
                move.add_direction(1, 0)
            elif key in self.bindings[2]:
                move.add_direction(0, -1)
            elif key in self.bindings[3]:
                move.add_direction(0, 1)

    def applied_on_entity(self, entity):
        self.entity = entity
        entity.event_manager.bind(KeyPressedEvent, self.key_pressed)
