import pygame
from pysmile.component import Component
from pysmile.components.transform import TransformComponent
from .tile import Tile
from pysmile.math.rect import Rect


class TileMap(Component):
    def __init__(self, tileset, size, tile_map=None):
        self.tile_size = None
        self.entity = None
        self.tileset = tileset
        self.size = size
        if tile_map is None:
            self.tile_map = []
        else:
            self.tile_map = tile_map

    def load_letters(self, tiles):
        self.tile_map = [[] for _ in range(len(tiles))]
        for i, row in enumerate(tiles):
            for col in row:
                self.tile_map[i].append([Tile(self.tileset.tiles[t], t, tiles) for t in col])

    def calculate_rects(self):
        pos = self.entity.get_component(TransformComponent).pos
        if not self.tile_map:
            return
        tile_width, tile_height = (self.size[0] / len(self.tile_map[0]), self.size[0] / len(self.tile_map))
        self.tile_size = (tile_width, tile_height)
        for y in range(len(self.tile_map)):
            for x in range(len(self.tile_map[y])):
                for i in range(len(self.tile_map[y][x])):
                    self.tile_map[y][x][i].rect = Rect(pos.x + x * tile_width,
                                                       pos.y + y * tile_height,
                                                       tile_width,
                                                       tile_height)

    def applied_on_entity(self, entity):
        self.entity = entity
        self.calculate_rects()

    def get_tiles_around(self, pos):
        if pos[0] < 0 or pos[1] < 0:
            return None
        if self.tile_size is None:
            return None

        start_pos = (int(pos[0] / self.tile_size[0]), int(pos[1] / self.tile_size[1]))
        res_tiles = [self.tile_map[start_pos[1]][start_pos[0]]]
        dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]
        for d in dirs:
            if 0 <= start_pos[0] + d[0] < len(self.tile_map[0]) and 0 <= start_pos[1] + d[1] < len(self.tile_map):
                res_tiles.append(self.tile_map[start_pos[1] + d[1]][start_pos[0] + d[0]])
        return res_tiles
