from elyria import Game, ResourceManager, GameObject, Animation, core, Input, Key
import glm
from glfw.GLFW import glfwGetTime
from enum import StrEnum


class Direction(StrEnum):
    UP         = "UP"
    UP_RIGHT   = "UP_RIGHT"
    RIGHT      = "RIGHT"
    DOWN_RIGHT = "DOWN_RIGHT"
    DOWN       = "DOWN"
    DOWN_LEFT  = "DOWN_LEFT"
    LEFT       = "LEFT"
    UP_LEFT    = "UP_LEFT"


class Player(GameObject):
    def __init__(self):
        animation = ResourceManager.get_animation("character")
        size = glm.vec2(animation.width * 5, animation.height * 5)
        position = glm.vec2((core.game.width - size.x) / 2.0, (core.game.height - size.y) / 2.0)
        super().__init__(
            position=position,
            rotation=0.0,
            size=size,
            animation=animation
        )
        self.direction = Direction.DOWN

    def update(self, dt: float) -> None:
        super().update(dt)

        new_direction = self.direction
        if Input.is_pressed(Key.Z):
            if Input.is_pressed(Key.Q):
                new_direction = Direction.UP_LEFT
            elif Input.is_pressed(Key.D):
                new_direction = Direction.UP_RIGHT
            else:
                new_direction = Direction.UP
        elif Input.is_pressed(Key.S):
            if Input.is_pressed(Key.Q):
                new_direction = Direction.DOWN_LEFT
            elif Input.is_pressed(Key.D):
                new_direction = Direction.DOWN_RIGHT
            else:
                new_direction = Direction.DOWN
        elif Input.is_pressed(Key.Q):
            new_direction = Direction.LEFT
        elif Input.is_pressed(Key.D):
            new_direction = Direction.RIGHT

        if new_direction != self.direction and self.animation:
            self.animation = ResourceManager.get_animation(f"character_{self.direction}")

        self.direction = new_direction
        

class SmallRPG(Game):
    def __init__(self):
        super().__init__(800, 600, "Small RPG")

    def init(self):
        super().init()

        ResourceManager.load_texture("textures/background.jpg", False, "background")

        # 128 * 288 pixels
        # 128 pixels de large et 8 frames par lignes, soit des sprites de 16 pixels
        # 288 pixels de haut et 12 frames par colonne, soit des sprites de 24 pixels
        characters = ResourceManager.load_texture("textures/characters.png", True, "characters")

        ResourceManager.load_animation(Animation(texture=characters,  row=9, frames=4, width=16, height=24, animation_speed=5), "character_up")
        ResourceManager.load_animation(Animation(texture=characters, row=10, frames=4, width=16, height=24, animation_speed=5), "character_up_right")
        ResourceManager.load_animation(Animation(texture=characters, row=11, frames=4, width=16, height=24, animation_speed=5), "character_right")
        ResourceManager.load_animation(Animation(texture=characters, row=12, frames=4, width=16, height=24, animation_speed=5), "character_down_right")
        ResourceManager.load_animation(Animation(texture=characters, row=13, frames=4, width=16, height=24, animation_speed=5), "character_down")
        ResourceManager.load_animation(Animation(texture=characters, row=14, frames=4, width=16, height=24, animation_speed=5), "character_down_left")
        ResourceManager.load_animation(Animation(texture=characters, row=14, frames=4, width=16, height=24, animation_speed=5), "character_left")
        ResourceManager.load_animation(Animation(texture=characters, row=15, frames=4, width=16, height=24, animation_speed=5), "character_up_left")



        self.player = Player()

    def update(self, dt: float):
        self.player.update(dt)

    def render(self):
        self.player.draw(self.renderer)

    def gui_render(self):
        # self.text.render_text("Hello Small RPG", 250.0, self.height / 2.0, 1.0)
        pass
