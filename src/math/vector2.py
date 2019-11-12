import pygame


class Vector2(pygame.Vector2):
    def __int__(self, x, y):
        if isinstance(x, tuple):
            super().__init__(x)
        elif isinstance(x, pygame.Vector2):
            super().__init__(x.x, x.y)
        else:
            super().__init__(x, y)

    @property
    def xy(self):
        return self.x, self.y
