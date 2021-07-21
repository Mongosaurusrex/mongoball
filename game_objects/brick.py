import pygame

from game_objects.images.sprite_resolvers import red_brick
from game_objects.ball import Ball


class BaseBrick(pygame.sprite.Sprite):
    def on_hit(self):
        pass

    def on_destroy(self):
        pass

    def destroy(self):
        self.on_hit()
        self.health -= 1
        if self.health == 0:
            self.on_destroy()
            self.kill()


class RedBrick(BaseBrick):
    def __init__(self, x_pos, y_pos):
        super().__init__()

        self.image = red_brick
        self.rect = pygame.Rect(x_pos, y_pos, 30, 25)
        self.health = 1
