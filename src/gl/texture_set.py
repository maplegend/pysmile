from .gl_texture import GLTexture

class TextureSet:
    """Texturesets contain and name textures."""

    def __init__(self):
        self.textures = {}

    def load(self, texname=None):
        self.textures[texname] = GLTexture(texname)

    def set(self, texname, data):
        self.textures[texname] = data

    def delete(self, texname):
        del self.textures[texname]

    def __del__(self):
        self.textures.clear()
        del self.textures

    def get(self, texname):
        return self.textures[texname]