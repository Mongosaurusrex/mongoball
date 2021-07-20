import pygame

from game_objects.images.sprite_resolvers import default_paddle


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.current_width = 73
        self.images = default_paddle
        self.animation_index = 0
        self.image = self.images[self.animation_index]
        self.rect = pygame.Rect(400, 550, self.current_width, 13)

    def update(self):
        self.animation_index += 1

        if self.animation_index >= len(self.images):
            self.animation_index = 0

        self.image = self.images[self.animation_index]

    def move_left(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self, pixels):
        self.rect.x += pixels
        if self.rect.x + self.current_width > 800:
            self.rect.x = 800 - self.current_width
