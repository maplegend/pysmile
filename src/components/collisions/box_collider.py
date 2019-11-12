from src.math.rect import Rect
from src.math.vector2 import Vector2
from .collider import Collider
from ..transform import TransformComponent


class BoxCollider(Collider):
    def __init__(self, size, offset=None):
        super().__init__()
        self.size = size
        self.entity = None
        self.offset = Vector2(0, 0) if offset is None else offset

    def applied_on_entity(self, entity):
        self.entity = entity
        super().applied_on_entity(entity)

    def get_collider(self):
        trans = self.entity.get_component(TransformComponent)
        return [Rect(trans.x+self.offset.x, trans.y+self.offset.y, self.size[0], self.size[1])]
