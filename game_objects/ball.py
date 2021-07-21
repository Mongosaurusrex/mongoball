import math

import pygame
from game_objects.images.sprite_resolvers import default_ball
from game_objects.paddle import Paddle
from game_objects.spark import Spark


class Ball(pygame.sprite.Sprite):
    def __init__(self, sprite_group: pygame.sprite.Group):
        super().__init__()

        self.sprite_group = sprite_group
        self.image = default_ball
        self.rect = pygame.Rect(400, 541, 9, 9)
        self.moving = False
        self.speed = 0.1

        self.velocity = [0, -100]

    def toggle_moving(self):
        self.moving = not self.moving

    def move_with_paddle(self, paddle: Paddle):
        self.rect.x = paddle.current_width / 2 + paddle.rect.x

    def update(self):
        if self.moving:
            self.rect.x += self.velocity[0] * self.speed
            self.rect.y += self.velocity[1] * self.speed

    def paddle_bounce(self, paddle: Paddle):
        min_vector = (-90, -10)

        x_vector = ((self.rect.x - paddle.rect.x) / paddle.current_width) * 180 + min_vector[0]
        y_vector = 0.0111111 * (math.pow(x_vector, 2)) - 100

        if self.speed < 0.2:
            self.speed += 0.005
        else:
            spark = Spark(self.rect.x - 9, 550 - 22.5)
            self.sprite_group.add(spark)

        self.velocity = [x_vector, y_vector]
