import pygame
from OpenGL.GL import *


class GLImage:
    def __init__(self, texture):
        self.texture = texture
        self.width = self.texture.width
        self.height = self.texture.height
        self.rect = pygame.Rect(0, 0, self.texture.width, self.texture.height)
        self.color = (1, 1, 1, 1)
        self.rotation = 0
        self.rotation_center = None

    def draw(self, rect):
        glColor4fv(self.color)

        glLoadIdentity()
        glTranslate(rect.x, rect.y, 0)

        glScalef(rect.width / (self.rect.width * 1.0), rect.height / (self.rect.height * 1.0), 1.0)

        if self.rotation != 0:
            if self.rotation_center is None:
                self.rotation_center = (self.rect.width / 2, self.rect.height / 2)
            # (w,h) = rotationCenter
            glTranslate(self.rotation_center[0], self.rotation_center[1], 0)
            glRotate(self.rotation, 0, 0, -1)
            glTranslate(-self.rotation_center[0], -self.rotation_center[1], 0)

        glCallList(self.texture.displaylist)

        if self.rotation != 0:  # reverse
            glTranslate(self.rotation_center[0], self.rotation_center[1], 0)
            glRotate(-self.rotation, 0, 0, -1)
            glTranslate(-self.rotation_center[0], -self.rotation_center[1], 0)
