from OpenGL.GL import *


class TileTexture:
    def __init__(self, rect):
        self.rect = rect
        self.display_list = None
        self.size = None

    @property
    def is_baked(self):
        return self.display_list is not None

    def bake(self, tileset, size):
        self.size = size
        self.display_list = glGenLists(1)
        glNewList(self.display_list, GL_COMPILE)
        self.render(tileset, size)
        glEndList()

    def render(self, tileset, size):
        x = self.rect.x / tileset.width
        y = 1. - self.rect.y / tileset.height
        w = self.rect.width / tileset.width
        h = self.rect.height / tileset.height
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        glBindTexture(GL_TEXTURE_2D, tileset.texture)

        # Draw the tile
        glBegin(GL_QUADS)

        # Upper left corner
        glTexCoord2f(x, y)
        glVertex2f(0, 0)

        # Lower left corner
        glTexCoord2f(x, y - h)
        glVertex2f(0,  size[1])

        # Lower right corner
        glTexCoord2f(x + w, y - h)
        glVertex2f(size[0], size[1])

        # Upper right corner
        glTexCoord2f(x + w, y)
        glVertex2f(size[0], 0)

        glEnd()


class AnimatedTileTexture(TileTexture):
    def __init__(self, rect, frames):
        super().__init__(rect)
        self.frames = frames
        self.display_lists = []

    @property
    def is_baked(self):
        return len(self.display_lists) > 0

    def bake(self, tileset, size):
        for f in range(self.frames):
            super().bake(tileset, size)
            self.rect.move_ip((self.rect.width, 0))
            self.display_lists.append(self.display_list)
        self.rect.move_ip((-self.rect.width*self.frames, 0))
