from src.game_component import GameComponent
from src.game_renderer import GameRender
from src.game_screen import GameScreen


class GameRendererComponent(GameComponent):
    def __init__(self, screen_size):
        super().__init__()
        self.exec_priority = -1
        self.renderer = None
        self.game_screen = GameScreen(screen_size)

    def applied_on_game(self, game):
        self.renderer = GameRender(game)

    def game_tick(self):
        self.renderer.draw()
