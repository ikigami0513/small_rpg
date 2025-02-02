from OpenGL.GL import *
from elyria.shader import Shader
from elyria.texture2d import Texture2D
import glm
import numpy as np


class SpriteRenderer:
    def __init__(self, shader: Shader) -> None:
        self.shader = shader
        self.quad_vao = None
        self.init_render_data()

    def draw_sprite(
        self,
        texture: Texture2D,
        position: glm.vec2,
        size: glm.vec2 = glm.vec2(10.0, 10.0),
        rotate: float = 0.0,
        color: glm.vec3 = glm.vec3(1.0)
    ) -> None:
        tex_width, tex_height = texture.width, texture.height
        self.draw_subsprite(texture, position, size, rotate, color, (0, 0, tex_width, tex_height))

    def draw_subsprite(
        self,
        texture: Texture2D,
        position: glm.vec2,
        size: glm.vec2 = glm.vec2(10.0, 10.0),
        rotate: float = 0.0,
        color: glm.vec3 = glm.vec3(1.0),
        tex_coords: tuple[int, int, int, int] = [0, 0, 0, 0]
    ) -> None:
        """
        Affiche une portion de la texture.
        tex_coords: (x, y, width, height) en pixels.
        """
        self.shader.use()

        model = glm.mat4(1.0)
        model = glm.translate(model, glm.vec3(position, 0.0))
        model = glm.translate(model, glm.vec3(0.5 * size.x, 0.5 * size.y, 0.0))
        model = glm.rotate(model, glm.radians(rotate), glm.vec3(0.0, 0.0, 1.0))
        model = glm.translate(model, glm.vec3(-0.5 * size.x, -0.5 * size.y, 0.0))
        model = glm.scale(model, glm.vec3(size, 1.0))

        self.shader.set_mat4("model", model)
        self.shader.set_vec3("spriteColor", color)

        glActiveTexture(GL_TEXTURE0)
        texture.bind()

        tex_x, tex_y, tex_w, tex_h = tex_coords
        tex_width, tex_height = texture.width, texture.height
        u0, v0 = tex_x / tex_width, tex_y / tex_height
        u1, v1 = (tex_x + tex_w) / tex_width, (tex_y + tex_h) / tex_height

        vertices = np.array([
            # pos    # tex
            0.0, 1.0, u0, v1,
            1.0, 0.0, u1, v0,
            0.0, 0.0, u0, v0,
            
            0.0, 1.0, u0, v1,
            1.0, 1.0, u1, v1,
            1.0, 0.0, u1, v0
        ], dtype=np.float32)

        glBindVertexArray(self.quad_vao)
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 4, GL_FLOAT, GL_FALSE, 4 * vertices.itemsize, None)
        
        glDrawArrays(GL_TRIANGLES, 0, 6)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

    def init_render_data(self) -> None:
        self.quad_vao = glGenVertexArrays(1)
        glBindVertexArray(self.quad_vao)
        glBindVertexArray(0)
