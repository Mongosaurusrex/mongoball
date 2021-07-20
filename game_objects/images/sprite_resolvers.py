import os
import pygame

default_paddle = [
    pygame.image.load(
        os.path.join(os.path.dirname(__file__), "paddle_default/0.png")
    ),
    pygame.image.load(
        os.path.join(os.path.dirname(__file__), "paddle_default/1.png")
    ),
    pygame.image.load(
        os.path.join(os.path.dirname(__file__), "paddle_default/2.png")
    ),
    pygame.image.load(
        os.path.join(os.path.dirname(__file__), "paddle_default/2.png")
    ),
]

default_ball = pygame.image.load(
    os.path.join(os.path.dirname(__file__), "ball/default.png")
)

fire_ball = pygame.image.load(
    os.path.join(os.path.dirname(__file__), "ball/fire.png")
)

life_image = pygame.image.load(
    os.path.join(os.path.dirname(__file__), "life/life.png")
)
