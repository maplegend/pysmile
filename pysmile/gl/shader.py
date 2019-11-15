from OpenGL.GL import *


class Shader:
    uniform_prefix = "uniform_"

    def __init__(self, vertex_code, fragment_code):
        self.program_id = glCreateProgram()
        self.uniforms = {}
        self.using = False
        vs_id = self.add_shader(vertex_code, GL_VERTEX_SHADER)
        frag_id = self.add_shader(fragment_code, GL_FRAGMENT_SHADER)

        glAttachShader(self.program_id, vs_id)
        glAttachShader(self.program_id, frag_id)
        glLinkProgram(self.program_id)

        if glGetProgramiv(self.program_id, GL_LINK_STATUS) != GL_TRUE:
            info = glGetProgramInfoLog(self.program_id)
            glDeleteProgram(self.program_id)
            glDeleteShader(vs_id)
            glDeleteShader(frag_id)
            raise RuntimeError('Error linking program: %s' % (info))
        glDeleteShader(vs_id)
        glDeleteShader(frag_id)

    def __setattr__(self, key, value):
        """Set custom uniform value like 'shader.uniform_value = value'. Now support only int and float"""
        if key.startswith(self.uniform_prefix):
            key = key[len(self.uniform_prefix):]
            loc = self.get_uniform_location(key)
            print(loc, key)
            if loc == -1:
                raise AttributeError

            if isinstance(value, float):
                self.uniforms[key] = (glUniform1f, loc, value)

            elif isinstance(value, int):
                self.uniforms[key] = (glUniform1i, loc, value)
            else:
                raise AttributeError

            if self.using:
                self.update_unifroms()
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, attr):
        """Return uniform value like 'shader.uniform_value'"""
        if attr.startswith(self.uniform_prefix):
            return self.get_uniform_location(attr[len(self.uniform_prefix):])
        else:
            return object.__getattribute__(self, attr)

    def update_unifroms(self):
        [u[0](u[1], u[2]) for _, u in self.uniforms.items()]

    def get_uniform_location(self, name):
        return glGetUniformLocation(self.program_id, name)

    def get_uniform_value(self, name):
        return self.uniforms[name][2]

    def use(self):
        self.using = True
        glUseProgram(self.program_id)
        self.update_unifroms()

    def unuse(self):
        self.using = False
        glUseProgram(0)

    @staticmethod
    def init_from_files(vert_path, frag_path):
        vert = open(vert_path, "r")
        frag = open(frag_path, "r")
        return Shader(vert.read(), frag.read())

    @staticmethod
    def add_shader(source, shader_type):
        shader_id = 0
        try:
            shader_id = glCreateShader(shader_type)
            glShaderSource(shader_id, source)
            glCompileShader(shader_id)
            if glGetShaderiv(shader_id, GL_COMPILE_STATUS) != GL_TRUE:
                info = glGetShaderInfoLog(shader_id)
                raise RuntimeError('Shader compilation failed: %s' % (info))
            return shader_id
        except RuntimeError:
            glDeleteShader(shader_id)
            raise
