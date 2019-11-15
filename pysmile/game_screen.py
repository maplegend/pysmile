import pygame
from OpenGL.GL import *
from OpenGL.GLU import *


class GameScreen:

    @staticmethod
    def find_best_size(w, h):
        modelist = pygame.display.list_modes()
        nextmode = [l for l in modelist if l[0] >= w and l[1] >= h]
        bestx, besty = -1, -1
        for l in nextmode:
            if (bestx == -1 or bestx >= l[0]) and (besty == -1 or besty >= l[1]):
                bestx, besty = l[0], l[1]

        print("resolution: ", bestx, besty)

        return bestx, besty

    def __init__(self, size):
        self.display_mod = pygame.OPENGL | pygame.DOUBLEBUF

        self.size = self.find_best_size(size[0], size[1])
        self.screen = pygame.display.set_mode(size, self.display_mod)
        # pygame.display.gl_set_attribute(pygame.GL_MAJOR_VERSION, 3)
        # pygame.display.gl_set_attribute(GL_MINOR_VERSION, 2)
        # pygame.display.gl_set_attribute(GL_CONTEXT_PROFILE_MASK, GL_CONTEXT_CORE_PROFILE_BIT)

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # this puts us in quadrant 1, rather than quadrant 4
        gluOrtho2D(0, size[0], size[1], 0)
        glMatrixMode(GL_MODELVIEW)

        # set up texturing
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.full_screen = False

    def toggle_full_screen(self):
        self.full_screen = not self.full_screen
        pygame.display.quit()
        pygame.display.init()
        if self.full_screen:
            self.screen = pygame.display.set_mode(self.size, self.display_mod | pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.display_mod)
