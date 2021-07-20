import pygame

from game_objects.images.sprite_resolvers import life_image


class Life(pygame.sprite.Sprite):
    def __init__(self, x_diff):
        super().__init__()

        self.image = life_image
        self.rect = pygame.Rect(800 - x_diff, 5, 18, 5)
