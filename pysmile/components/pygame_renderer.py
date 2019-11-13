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
        self.need_redraw = True
        self.displaylist = None

    def render(self, rect, entity):
        if self.need_redraw:
            glLoadIdentity()

            img = self.renderer.render(entity, rect)
            w, h = img.get_size()
            texture = glGenTextures(1)
            glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
            glBindTexture(GL_TEXTURE_2D, texture)
            glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
            data = pygame.image.tostring(img, "RGBA", 1)
            glTexImage2D(GL_TEXTURE_2D, 0, 4, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)

            newlist = glGenLists(1)
            glNewList(newlist, GL_COMPILE)
            glBindTexture(GL_TEXTURE_2D, texture)
            glBegin(GL_QUADS)

            # Bottom Left Of The Texture and Quad
            glTexCoord2f(0, 1)
            glVertex2f(0, 0)

            # Top Left Of The Texture and Quad
            glTexCoord2f(0, 0)
            glVertex2f(0, rect.height)

            # Top Right Of The Texture and Quad
            glTexCoord2f(1, 0)
            glVertex2f(rect.width, rect.height)

            # Bottom Right Of The Texture and Quad
            glTexCoord2f(1, 1)
            glVertex2f(rect.width, 0)
            glEnd()
            glEndList()
            self.displaylist = newlist
            self.need_redraw = False

        glColor4fv((1, 1, 1, 1))

        glLoadIdentity()
        glTranslate(rect.x, rect.y, 0)

        glCallList(self.displaylist)
        glTranslate(-rect.x, -rect.y, 0)
