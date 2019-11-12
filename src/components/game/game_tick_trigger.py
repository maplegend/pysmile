from src.game_component import GameComponent
from .game_event_manager import GameEventManagerComponent
from src.events.update import UpdateEvent


class GameTickTriggerComponent(GameComponent):
    def __init__(self):
        super().__init__()
        self.exec_priority = 0

    def game_tick(self):
        em = self.game.get_component(GameEventManagerComponent)
        if em is None:
            return

        em.trigger_event(UpdateEvent())
