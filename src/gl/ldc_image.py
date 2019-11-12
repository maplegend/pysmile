from OpenGL.GL import *


class LDCTextureEntry:
    def __init__(self, texture, position):
        self.texture = texture
        self.position = position


class LDCImage:
    """Limited Dynamic Composite Image. LDCImage uses only the
    texture display lists for drawing, which makes it useful for simpler
    applications like text and tiles that don't need the features of DCImage.

    Remember not to mistake this for *LCD* Image!"""

    def __init__(self, entries):
        self.entries = entries

    def draw(self, abspos):
        glLoadIdentity()
        glTranslate(abspos[0], abspos[1], 0)

        for c in self.entries:
            glTranslate(c[0].x, c[0].y, 0)
            glCallList(c[1].displaylist)
            glTranslate(-c[0].x, -c[0].y, 0)
