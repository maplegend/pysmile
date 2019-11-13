from abc import ABC, abstractmethod


class Renderer(ABC):
    def __init__(self):
        super().__init__()
        self.rendering_size = None

    @abstractmethod
    def render(self, entity, rect):
        pass


class PyGameRenderer(Renderer, ABC):
    pass
