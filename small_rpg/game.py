from elyria import Game, ResourceManager, GameObject, Animation, core
import glm
from glfw.GLFW import glfwGetTime

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

class SmallRPG(Game):
    def __init__(self):
        super().__init__(800, 600, "Small RPG")

    def init(self):
        super().init()

        ResourceManager.load_texture("textures/background.jpg", False, "background")

        # 128 * 288 pixels
        # 128 pixels de large et 8 frames par lignes, soit des sprites de 16 pixels
        # 288 pixels de haut et 12 frames par colonne, soit des sprites de 24 pixels
        ResourceManager.load_texture("textures/characters.png", True, "characters")

        ResourceManager.load_animation(Animation(
            texture=ResourceManager.get_texture("characters"),
            row=9,
            frames=4,
            width=16,
            height=24,
            animation_speed=5
        ), "character")

        self.player = Player()

    def update(self, dt: float):
        self.player.update(dt)

    def render(self):
        self.player.draw(self.renderer)

    def gui_render(self):
        # self.text.render_text("Hello Small RPG", 250.0, self.height / 2.0, 1.0)
        pass
