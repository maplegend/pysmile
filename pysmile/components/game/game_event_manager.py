from pysmile.game_component import GameComponent
from pysmile.event_manager import EventManager


class GameEventManagerComponent(GameComponent):
    def __init__(self):
        super().__init__()

        self.event_manager = EventManager()

    def trigger_event(self, event):
        self.event_manager.trigger_event(event)

    def bind(self, event, callback):
        self.event_manager.bind(event, callback)

    def game_tick(self):
        pass
