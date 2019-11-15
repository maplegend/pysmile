import pygame
from pysmile.game_component import GameComponent
from .game_event_manager import GameEventManagerComponent
from pysmile.events.key_pressed import KeyPressedEvent


class GameKeyPressComponent(GameComponent):
    def __init__(self):
        super().__init__()
        self.exec_priority = 1

    def game_tick(self):
        em = self.game.get_component(GameEventManagerComponent)
        if em is None:
            return

        for i in range(len(pygame.key.get_pressed())):
            if pygame.key.get_pressed()[i] != 0:
                em.trigger_event(KeyPressedEvent(i))
