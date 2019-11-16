import pygame
from pysmile.component import Component
from .collider import Collider
from pysmile.events.hover import HoverEvent
from pysmile.events.click import ClickEvent
from pysmile.events.update import UpdateEvent


class MouseColliderComponent(Component):
    def __init__(self):
        self.entity = None

    def update(self, event):
        collider = self.entity.get_component(Collider).get_collider()
        if not collider:
            return

        pos = pygame.mouse.get_pos()
        buttons = pygame.mouse.get_pressed()
        for col in collider:
            if col.collidepoint(pos):
                self.entity.event_manager.trigger_event(HoverEvent(self.entity))
                if True in buttons:
                    self.entity.event_manager.trigger_event(ClickEvent(self.entity, buttons, pos))

    def applied_on_entity(self, entity):
        self.entity = entity
        entity.event_manager.bind(UpdateEvent, self.update)
