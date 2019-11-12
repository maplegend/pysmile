import pygame
import random
from src.game import Game
from src.entity import Entity
from src.components.renderer import RendererComponent
from src.components.transform import TransformComponent
from src.components.exit_on_escape import ExitOnEscape
from src.components.move import MoveComponent
from src.components.key_control import KeyControlComponent
from src.components.collisions.tile_map_collider import TileMapCollider
from src.components.collisions.box_collider import BoxCollider
from src.components.name import NameComponent
from src.tilemap.tilemap import TileMap
from src.tilemap.tileset import TileSet
from src.tilemap.tilemap_renderer import TileMapRenderer
from src.renderers.tile_renderer import TileRenderer
from src.math.vector2 import Vector2
from src.renderers.image_renderer import ImageRenderer


class PyDungeons:

    @staticmethod
    def build_wall_rect(map, rect):
        for y in range(rect.height):
            if y == 0 or y == rect.height-1:
                for x in range(0, rect.width):
                    map[rect.y + y][rect.x + x] = ["wall_mid"]
                    map[rect.y + y-1][rect.x + x] = ["floor_1", "wall_top_mid"]
            if y == rect.height - 1:
                continue
            map[rect.y + y][rect.x] = ["floor_1", "wall_side_mid_right"]
            map[rect.y + y][rect.right-1] = ["floor_1", "wall_side_mid_left"]

        map[rect.y-1][rect.x] = ["floor_1", "wall_corner_top_left"]
        map[rect.y][rect.x] = ["wall_corner_left"]

        map[rect.y - 1][rect.right-1] = ["floor_1", "wall_corner_top_right"]
        map[rect.y][rect.right-1] = ["wall_corner_right"]

        map[rect.bottom-2][rect.x] = ["floor_1", "wall_corner_bottom_left"]
        map[rect.bottom-2][rect.right - 1] = ["floor_1", "wall_corner_bottom_right"]

    @staticmethod
    def start():
        pygame.init()
        pygame.display.set_caption('PyDungeon')
        size = width, height = (640, 480)
        game = Game()
        game.setup_default_components(size)
        scene = game.scene

        tilemap = Entity()
        scene.add_entity(tilemap)
        tilemap.add_component(NameComponent("tilemap"))

        tilemap.add_component(TransformComponent(Vector2(0, 0)))

        ts = TileSet()
        ts.load("./assets/tileset.png", "./assets/tileinfo.info")
        tm = TileMap(ts, size)
        mp = [[["floor_"+str(random.randrange(1, 8))] for _ in range(24)] for _ in range(24)]
        PyDungeons.build_wall_rect(mp, pygame.Rect(2, 2, 10, 10))
        tm.load_letters(mp)
        tilemap.add_component(tm)
        tilemap.add_component(TileMapCollider(tm, ["wall_mid", "wall_side_mid_right", "wall_side_mid_left"]))
        tilemap.add_component(RendererComponent(TileMapRenderer(), size))

        player = Entity()
        scene.add_entity(player)
        player.add_component(NameComponent("player"))

        key_bindings = [[pygame.K_a], [pygame.K_d], [pygame.K_w], [pygame.K_s]]

        player.add_component(MoveComponent(1, 2))
        player.add_component(KeyControlComponent(key_bindings))
        #player.add_component(ScreenBoundsCollisionHandler(pygame.Rect(0, 0, width, height)))
        player.add_component(TransformComponent(Vector2(100, 100)))
        player.add_component(BoxCollider((16*2, 22*2), Vector2(0, 12)))
        player.add_component(RendererComponent(TileRenderer(ts.tiles["knight_f_idle_anim"], ts), (16*2, 28*2)))
        #player.add_component(RendererComponent(ImageRenderer("assets/tileset.png"), (1000, 1000)))

        game.add_component(ExitOnEscape())

        game.run()

