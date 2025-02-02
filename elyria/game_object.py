import glm
from elyria.texture2d import Texture2D
from elyria.animation import Animation
from elyria.sprite_renderer import SpriteRenderer
from typing import Optional


# Container object for holding all state relevant for a single
# game object entity. Each object in the game likely needs the
# minimal of state as described within GameObject.
class GameObject:
    def __init__(
        self,
        position: glm.vec2 = glm.vec2(0.0, 0.0),
        rotation: float = 0.0,
        size: glm.vec2 = glm.vec2(1.0, 1.0),
        texture: Optional[Texture2D] = None,
        animation: Optional[Animation] = None,
        color: glm.vec3 = glm.vec3(1.0),
        velocity: glm.vec2 = glm.vec2(0.0, 0.0),
        is_solid: bool = False,
        destroyed: bool = False
    ):
        self.position = position
        self.rotation = rotation
        self.size = size
        self.texture = texture
        self.animation = animation
        self.color = color
        self.velocity = velocity
        self.is_solid = is_solid
        self.destroyed = destroyed

    def update(self, dt):
        if self.animation:
            self.animation.update(dt)

    def draw(self, renderer: SpriteRenderer) -> None:
        if self.animation:
            renderer.draw_subsprite(
                self.animation.texture,
                self.position,
                self.size,
                self.rotation,
                self.color,
                tex_coords=[self.animation.width * int(self.animation.frame), (self.animation.row - 1) * self.animation.height, self.animation.width, self.animation.height]
            )
        elif self.texture:
            renderer.draw_sprite(
                self.texture,
                self.position,
                self.size,
                self.rotation,
                self.color
            )

