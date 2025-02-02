from elyria.texture2d import Texture2D
from elyria.sprite_renderer import SpriteRenderer


class Animation:
    def __init__(self, texture: Texture2D, row: int, frames: int, width: int, height: int, animation_speed: int, is_vertical: bool = False):
        self.texture = texture
        self.row = row
        self.frames = frames
        self.frame = 0.0
        self.width = width
        self.height = height
        self.animation_speed = animation_speed
        self.is_vertical = is_vertical

    def update(self, dt: float) -> None:
        self.frame += (self.animation_speed * dt)
        if int(self.frame) >= self.frames:
            self.frame = 0.0
