from src.gl.gl_texture import GLTexture
from src.math.rect import Rect
from .tile_texture import TileTexture, AnimatedTileTexture


class TileSet:
    def __init__(self):
        self.tiles = {}
        self.colliders = {}
        self.texture, self.width, self.height = None, 0, 0

    def load(self, tex_name, tiles_info_file):
        self.texture, self.width, self.height = GLTexture.load_image(tex_name)
        f = open(tiles_info_file, "r")
        for line in f.readlines():
            if line == '':
                continue

            tile = line.split(' ')
            nums = [int(n) for n in tile[1:] if n != '']
            nlength = len(nums)
            if nlength == 4 or nlength == 8:
                self.tiles[tile[0]] = TileTexture(Rect(*nums[:4]))
            elif nlength == 5 or nlength == 9:
                self.tiles[tile[0]] = AnimatedTileTexture(Rect(*nums[:4]), nums[4])

            if nlength == 8 or nlength == 9:
                rect = Rect(*nums[4:8]) if nlength == 8 else Rect(*nums[5:9])
                self.colliders[tile[0]] = rect
