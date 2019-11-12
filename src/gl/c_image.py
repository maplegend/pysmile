from OpenGL.GL import *


class CImage:
    """CImage is a "composed image" that refs multiple GLImages.
    format is [(GLImage,argstoimage)...()..()]
    Cimage is fast but immutable - it has to recreate
    the display list to be changed."""

    def __init__(self, ilist):
        newlist = glGenLists(1)
        glNewList(newlist, GL_COMPILE)

        # see GLImage.draw
        for i in ilist:
            if i[1][0] is None:
                i[0].draw(i[1])
            else:  # absolute positioning normally resets the identity
                i[0].draw(i[1])
                glTranslate(-i[1].x, -i[1].y, 0)

        glEndList()
        self.displaylist = newlist

    def __del__(self):
        if hasattr(self, "displaylist") and self.displaylist is not None:
            self.del_dl(self.displaylist)
            self.displaylist = None

    def draw(self, abspos=None, relpos=None):
        if abspos:
            glLoadIdentity()
            glTranslate(abspos[0], abspos[1], 0)
        elif relpos:
            glTranslate(relpos[0], relpos[1], 0)

        glCallList(self.displaylist)

    @staticmethod
    def del_dl(d_list):
        glDeleteLists(d_list, 1)
