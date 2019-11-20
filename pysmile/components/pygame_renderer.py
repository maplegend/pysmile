import pygame
from .renderer import RendererComponent
from OpenGL.GL import *


class PyGameRendererComponent(RendererComponent):
    def __init__(self, renderer, size):
        """
        Render pygame surface to OpenGL display
        :param renderer: renderer that will be used to render entity
        :param size: entity's size that will be displayed
        """
        super().__init__(renderer, size)
        self.displaylist = None
        self.texture = None

    def render(self, rect, entity):
        if self.renderer.need_redraw:
            if self.texture is not None:
                glDeleteTextures([self.texture])

            img = self.renderer.render(entity, rect)
            w, h = img.get_size()
            self.texture = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
            glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
            data = pygame.image.tostring(img, "RGBA", 1)
            glTexImage2D(GL_TEXTURE_2D, 0, 4, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)

            self.displaylist = glGenLists(1)
            glNewList(self.displaylist, GL_COMPILE)
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glEnable(GL_TEXTURE_2D)
            glBegin(GL_QUADS)
            glTexCoord2f(0, 1)
            glVertex2f(0, 0)
            glTexCoord2f(1, 1)
            glVertex2f(0 + w, 0)
            glTexCoord2f(1, 0)
            glVertex2f(0 + w, 0 + h)
            glTexCoord2f(0, 0)
            glVertex2f(0, 0 + h)
            glEnd()
            glDisable(GL_TEXTURE_2D)
            glEndList()

            self.renderer.need_redraw = False

        glPushMatrix()
        glColor4fv((1, 1, 1, 1))
        glTranslate(rect.x, rect.y, 0)
        glCallList(self.displaylist)
        glPopMatrix()
