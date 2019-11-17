from ..renderer import Renderer
from pysmile.gl.gl_texture import GLTexture
from OpenGL.GL import *


class RectRenderer(Renderer):
    def __init__(self, color):
        self.color = color

    def render(self, entity, rect):
        glPushMatrix()
        glColor3f(*self.color.to_float()[:3])
        glRectd(*rect.xy, rect.right, rect.bottom)
        glPopMatrix()
