import pygame
from pysmile.renderer import Renderer
from pysmile.tilemap.tile_texture import AnimatedTileTexture
from OpenGL.GL import *


class TileRenderer(Renderer):
    def __init__(self, tile, tileset, animate=True):
        self.tile = tile
        self.tileset = tileset
        self.frame = 0
        self.animate = animate
        self.flip = False

    def render(self, entity, rect):
        if not self.tile.is_baked or self.tile.size != rect.size:
            self.tile.bake(self.tileset, rect.size)

        self.render_tile(self.tile, pygame.Vector2(rect.x, rect.y), int(self.frame), self.flip)
        if self.animate and isinstance(self.tile, AnimatedTileTexture):
            self.frame += 0.1
            if int(self.frame) >= self.tile.frames:
                self.frame = 0

    @staticmethod
    def render_tile(tile, pos, frame=0, flip=False):
        glPushMatrix()
        glTranslate(pos.x + (tile.size[0] if flip else 0), pos.y, 0)
        if flip:
            glScalef(-1., 1., 1.)

        if frame > 0:
            glCallList(tile.display_lists[frame])
        else:
            glCallList(tile.display_list)
        glPopMatrix()

