import pygame
from ..renderer import Renderer
from pysmile.gl.c_image import CImage
from pysmile.gl.gl_texture import GLTexture
from OpenGL.GL import *


class ImageRenderer(Renderer):
    def __init__(self, image):
        self.texture = GLTexture(image)
        self.rotation = None
        self.rotation_center = None

    def render(self, entity, rect):
        if rect.width != self.texture.width or rect.height != self.texture.height:
            newlist = glGenLists(1)
            glNewList(newlist, GL_COMPILE)
            glLoadIdentity()

            if self.rotation is not None and self.rotation != 0:
                if self.rotation_center is None:
                    self.rotation_center = (self.texture.width / 2, self.texture.height / 2)
                # (w,h) = rotationCenter
                glTranslate(self.rotation_center[0], self.rotation_center[1], 0)
                glRotate(self.rotation, 0, 0, -1)
                glTranslate(-self.rotation_center[0], -self.rotation_center[1], 0)

            glScalef(rect.width / (self.texture.width * 1.0), rect.height / (self.texture.height * 1.0), 1.0)

            self.texture.width, self.texture.height = rect.width, rect.height

            glCallList(self.texture.displaylist)
            glEndList()
            self.texture.displaylist = newlist

        glColor4fv((1, 1, 1, 1))

        glLoadIdentity()
        glTranslate(rect.x, rect.y, 0)

        glCallList(self.texture.displaylist)
        glTranslate(-rect.x, -rect.y, 0)
