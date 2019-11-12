from abc import ABC, abstractmethod
from .component import Component


class GameComponent(Component, ABC):
    def __init__(self):
        super().__init__()
        self.game = None
        self.exec_priority = 0

    def applied_on_entity(self, entity):
        from .game import Game
        if not isinstance(entity, Game):
            raise Exception("Entity must be a game")

        self.game = entity
        self.applied_on_game(entity)

    def applied_on_game(self, game):
        pass

    @abstractmethod
    def game_tick(self):
        pass
