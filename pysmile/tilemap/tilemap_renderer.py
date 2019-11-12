import pygame
from pysmile.renderer import Renderer
from pysmile.renderers.tile_renderer import TileRenderer
from .tilemap import TileMap
from OpenGL.GL import *


class TileMapRenderer(Renderer):
    def __init__(self, size=None):
        self.size = size
        self.tm_hash = None
        self.dl = None

    def render(self, entity, rect):
        tmap = entity.get_component(TileMap)
        if map is None:
            return
        tm = tmap.tile_map
        if self.tm_hash != str(tm) or self.dl is None:
            self.tm_hash = str(tm)
            self.dl = glGenLists(1)
            glNewList(self.dl, GL_COMPILE)
            glEnable(GL_TEXTURE_2D)
            glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)

            for row in tm:
                for tiles in row:
                    for tile in tiles:
                        glTranslate(tile.rect.x, tile.rect.y, 0)
                        tile.texture.render(tmap.tileset, (tile.rect.width, tile.rect.height))
                        glTranslate(-tile.rect.x, -tile.rect.y, 0)
            glEndList()
        glCallList(self.dl)



