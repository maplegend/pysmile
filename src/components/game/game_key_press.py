import pygame
from src.game_component import GameComponent
from .game_event_manager import GameEventManagerComponent
from src.events.key_pressed import KeyPressedEvent


class GameKeyPressComponent(GameComponent):
    def __init__(self):
        super().__init__()
        self.exec_priority = 1

    def game_tick(self):
        em = self.game.get_component(GameEventManagerComponent)
        if em is None:
            return

        for i, k in enumerate(pygame.key.get_pressed()):
            if k != 0:
                em.trigger_event(KeyPressedEvent(i))
