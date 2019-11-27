from OpenGL.GL import *
from collections import Iterable


class Shader:
    uniform_prefix = "uniform_"

    def __init__(self, vertex_code, fragment_code, inject_rect=True):
        self.program_id = glCreateProgram()
        self.uniforms = {}
        self.using = False
        self.inject_rect = inject_rect
        vs_id = self.add_shader(vertex_code, GL_VERTEX_SHADER)
        frag_id = self.add_shader(fragment_code, GL_FRAGMENT_SHADER)

        glAttachShader(self.program_id, vs_id)
        glAttachShader(self.program_id, frag_id)
        glBindAttribLocation(self.program_id, 0, "in_Position")
        glBindAttribLocation(self.program_id, 1, "in_Color")
        glLinkProgram(self.program_id)

        if glGetProgramiv(self.program_id, GL_LINK_STATUS) != GL_TRUE:
            info = glGetProgramInfoLog(self.program_id)
            glDeleteProgram(self.program_id)
            glDeleteShader(vs_id)
            glDeleteShader(frag_id)
            raise RuntimeError('Error linking program: %s' % info)
        glDeleteShader(vs_id)
        glDeleteShader(frag_id)

    def __setattr__(self, key, value):
        """Set custom uniform value like 'shader.uniform_value = value'. Now support only int, float and vectors"""
        if key.startswith(self.uniform_prefix):
            key = key[len(self.uniform_prefix):]
            self.set_uniform(key, value)
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, attr):
        """Return uniform value like 'shader.uniform_value'"""
        if attr.startswith(self.uniform_prefix):
            return self.get_uniform_location(attr[len(self.uniform_prefix):])
        else:
            return object.__getattribute__(self, attr)

    def set_uniform(self, key, value):
        loc = self.get_uniform_location(key)
        if loc == -1:
            print("Set uniform {} with value {} failed".format(key, value))
            return -1

        fu = None  # GL function
        if isinstance(value, float):
            fu = glUniform1f
        elif isinstance(value, int):
            fu = glUniform1i
        elif isinstance(value, tuple):
            if isinstance(value[0], float):
                if len(value) == 2:
                    fu = glUniform2f
                elif len(value) == 3:
                    fu = glUniform3f
                elif len(value) == 4:
                    fu = glUniform4f
            elif isinstance(value[0], int):
                if len(value) == 2:
                    fu = glUniform2i
                elif len(value) == 3:
                    fu = glUniform3i
                elif len(value) == 4:
                    fu = glUniform4i

        if fu is None:
            print("Invalid value {}".format(value))
            raise AttributeError

        self.uniforms[key] = (fu, loc, value)

        if self.using:
            self.update_unifroms()

    def update_unifroms(self):
        for _, u in self.uniforms.items():
            if isinstance(u[2], Iterable):
                u[0](u[1], *u[2])
            else:
                u[0](u[1], u[2])

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
