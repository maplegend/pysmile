import pygame
from .entity import Entity
from .game_component import GameComponent
from .scene import Scene
from pysmile.components.game.collision_handler import GameCollisionsHandlerComponent
from .components.game.game_event_manager import GameEventManagerComponent
from .components.game.game_event_handler import GameEventHandlerComponent
from .components.game.game_key_press import GameKeyPressComponent
from .components.game.game_tick_trigger import GameTickTriggerComponent
from .components.game.game_render import GameRendererComponent


class Game(Entity):
    def __init__(self, scene=Scene):
        super().__init__()

        self.scene = scene(self)

        self.cached = []
        self.chash = 0
        self.running = True

    @property
    def screen_size(self):
        return self.get_component(GameRendererComponent).game_screen.size

    def setup_default_components(self, screen_size):
        self.add_component(GameEventManagerComponent())
        self.add_component(GameEventHandlerComponent())
        self.add_component(GameKeyPressComponent())
        self.add_component(GameTickTriggerComponent())
        self.add_component(GameRendererComponent(screen_size))
        self.add_component(GameCollisionsHandlerComponent())

    def game_tick(self):
        comps = self.get_components(GameComponent)
        nhash = hash(tuple(comps))
        if self.chash != nhash:
            self.chash = nhash
            self.cached = comps

        for comp in comps:
            comp.game_tick()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            self.game_tick()
            clock.tick(60)

    def exit(self):
        self.running = False
