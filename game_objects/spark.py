import pygame
from game_objects.images.sprite_resolvers import spark

class Spark(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()

        self.animation_index = 0
        self.nth_frame = 3
        self.current_frame = 1
        self.images = spark
        self.image = self.images[self.animation_index]
        self.rect = pygame.Rect(x_pos, y_pos, 55, 55)

    def update(self):
        if self.current_frame < self.nth_frame:
            self.current_frame += 1
            return

        self.animation_index += 1

        if self.animation_index >= len(self.images) - 1:
            self.kill()

        self.image = self.images[self.animation_index]
        self.current_frame = 1
