from .component_storage import ComponentStorage
from src.components.game.game_event_manager import GameEventManagerComponent


class Entity:
    def __init__(self):
        self._storage = ComponentStorage()
        self.scene = None

    def add_component(self, component):
        component.applied_on_entity(self)
        self._storage.add_component(component)

    def remove_component(self, component):
        self._storage.remove_component(component)

    def contains_component(self, component):
        return self._storage.contains_component(component)

    def get_component(self, component):
        comps = self._storage.get_component(component)
        if comps is None:
            return None
        return comps[0]

    def get_components(self, component):
        return self._storage.get_component(component)

    @property
    def event_manager(self):
        return self.scene.game.get_component(GameEventManagerComponent)
