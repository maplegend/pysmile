from abc import ABC


class Component(ABC):
    def applied_on_entity(self, entity):
        pass

    def removed(self):
        pass
