from abc import ABC, abstractmethod
from ..component import Component


class RendererEffect(Component, ABC):
    @abstractmethod
    def process(self, img):
        pass
