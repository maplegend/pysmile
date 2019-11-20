import pygame
import sys
from pysmile.game_component import GameComponent
from pysmile.events.key_press import KeyPressEvent
from pysmile.events.pygame_event import PyGameEvent
from .game_event_manager import GameEventManagerComponent


class GameEventHandlerComponent(GameComponent):
    def __init__(self):
        super().__init__()
        self.exec_priority = 1

    def game_tick(self):
        em = self.game.get_component(GameEventManagerComponent)
        if em is None:
            return

        for event in pygame.event.get():
            em.trigger_event(PyGameEvent(event))
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                em.trigger_event(KeyPressEvent(event.key))
