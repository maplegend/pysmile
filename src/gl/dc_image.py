from OpenGL.GL import *


class DCImage:
    """Dynamic Composite Image - elements are mutable, at the caveat of
    runtime performance."""

    def __init__(self, ilist):
        self.ilist = ilist

    def draw(self, abspos):
        glLoadIdentity()
        glTranslate(abspos[0], abspos[1], 0)

        for i in self.ilist:
            i[0].draw(i[1])
