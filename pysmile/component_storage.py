class ComponentAlreadyExistsException(Exception):
    """Raised when component already exists in storage"""
    pass


class ComponentStorage:
    def __init__(self):
        self._components = []

    def add_component(self, component):
        if component in self._components:
            raise ComponentAlreadyExistsException()
        self._components.append(component)

    def remove_component(self, component):
        self._components = [cm for cm in self._components if not isinstance(cm, component)]

    def contains_component(self, component):
        return self.get_component(component) is not None

    def get_components(self):
        return self._components

    def get_component(self, component):
        comps = [c for c in self._components if isinstance(c, component)]
        if not comps:
            return None
        return comps
