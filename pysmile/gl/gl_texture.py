import pygame
from OpenGL.GL import *


class GLTexture:
    def __init__(self, texname=None):
        self.texture, self.width, self.height = self.load_image(texname)
        self.displaylist = self.create_tex_dl(self.texture, self.width, self.height)

    def __del__(self):
        if hasattr(self, "texture") and self.texture is not None:
            self.del_texture(self.texture)
            self.texture = None
        if hasattr(self, "displaylist") and self.displaylist is not None:
            self.del_dl(self.displaylist)
            self.displaylist = None

    def __repr__(self):
        return self.texture.__repr__()

    @staticmethod
    def del_dl(d_list):
        glDeleteLists(d_list, 1)

    @staticmethod
    def load_image(image):
        texture_surface = pygame.image.load(image)

        texture_data = pygame.image.tostring(texture_surface, "RGBA", 1)

        width = texture_surface.get_width()
        height = texture_surface.get_height()

        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA,
                     GL_UNSIGNED_BYTE, texture_data)

        return texture, width, height

    @staticmethod
    def clip_surface(surface, rect):
        texture_surface = surface.subsurface(rect)

        texture_data = pygame.image.tostring(texture_surface, "RGBA", 1)

        width = texture_surface.get_width()
        height = texture_surface.get_height()

        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA,
                     GL_UNSIGNED_BYTE, texture_data)

        return texture, width, height

    @staticmethod
    def del_texture(texture):
        glDeleteTextures(texture)

    @staticmethod
    def create_tex_dl(texture, width, height):
        new_list = glGenLists(1)
        glNewList(new_list, GL_COMPILE)
        GLTexture.render_texture(texture, (width, height))
        glEndList()

        return new_list

    @staticmethod
    def render_texture(texture, size):
        glBindTexture(GL_TEXTURE_2D, texture)
        glBegin(GL_QUADS)

        # Bottom Left Of The Texture and Quad
        glTexCoord2f(0, 1)
        glVertex2f(0, 0)

        # Top Left Of The Texture and Quad
        glTexCoord2f(0, 0)
        glVertex2f(0, size[1])

        # Top Right Of The Texture and Quad
        glTexCoord2f(1, 0)
        glVertex2f(size[0], size[1])

        # Bottom Right Of The Texture and Quad
        glTexCoord2f(1, 1)
        glVertex2f(size[0], 0)
        glEnd()
