from ..component import Component


class TransformComponent(Component):
    def __init__(self, pos):
        super().__init__()
        self.position = pos

    @property
    def pos(self):
        return self.position

    @property
    def xy(self):
        return self.position.xy

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y
