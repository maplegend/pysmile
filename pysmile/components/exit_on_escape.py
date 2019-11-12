import pygame
import sys
from ..component import Component
from ..events.key_pressed import KeyPressedEvent


class ExitOnEscape(Component):
    def applied_on_entity(self, entity):
        entity.event_manager.bind(KeyPressedEvent, lambda event: sys.exit() if event.key == pygame.K_ESCAPE else None)
