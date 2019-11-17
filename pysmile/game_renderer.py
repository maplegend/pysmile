import pygame
from OpenGL.GL import *
from .components.renderer import RendererComponent
from .components.transform import TransformComponent
from .stopwatch import Stopwatch
from .math.rect import Rect


class GameRender:
    def __init__(self, game):
        self.game = game
        self.stopwatch = Stopwatch()
        self.ticks = 0

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        screen_size = self.game.screen_size
        for ent in self.game.scene.get_entities_with_component(RendererComponent):
            rend = ent.get_component(RendererComponent)
            trans = ent.get_component(TransformComponent)
            if not rend or not trans:
                continue
            if rend.shader is not None:
                rend.shader.uniform_rect = (trans.x, screen_size[1] - trans.y - rend.size[1], *rend.size)
                rend.shader.use()
            rend.render(Rect(*trans.xy, *rend.size), ent)
            if rend.shader is not None:
                rend.shader.unuse()

        er = glGetError()
        if er != 0:
            print("ERROR: GL error: {}".format(er))

        pygame.display.flip()
        self.ticks += 1
