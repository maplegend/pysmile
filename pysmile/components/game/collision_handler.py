import pygame
from pysmile.math.rect import Rect
from pysmile.game_component import GameComponent


class GameCollisionsHandlerComponent(GameComponent):
    def __init__(self):
        self.colliders = []
        self.rects = set()
        self.chunk_size = 100
        self.static_collision_map = {}

    def check_rect_collision(self, rect, exceptions=None):
        if exceptions is None:
            exceptions = []
        colls = set()
        for c in rect.corners:
            rects = self._get_rects_by_position(c)
            if rects is not None:
                colls.update(rects)
        colls.update(self.rects)
        for col in colls:
            if rect != col and col not in exceptions and rect.colliderect(col):
                return True
        return False

    def check_line_collision(self, line):
        for coll in self.colliders:
            if isinstance(coll, Rect):
                return coll.intersect_line(line)

            for rect in coll:
                intr = rect.intersect_line(line)
                if intr is not None:
                    return intr
            return None

    def add_collider(self, collider):
        self.colliders.append(collider)

    def _get_rects_by_position(self, position):
        pos = (position[0] // self.chunk_size, position[1] // self.chunk_size)
        if pos in self.static_collision_map:
            return self.static_collision_map[pos]
        return None

    def _add_rect_by_position(self, position, rect):
        pos = (position[0] // self.chunk_size, position[1] // self.chunk_size)
        if pos not in self.static_collision_map:
            self.static_collision_map[pos] = set()

        self.static_collision_map[pos].add(rect)

    def add_static_collider(self, collider):
        for r in collider.get_collider():
            [self._add_rect_by_position(c, r) for c in r.corners]

    def game_tick(self):
        self.rects = set()
        [self.rects.update(col.get_collider()) for col in self.colliders]
