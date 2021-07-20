import pygame

from common.constants import WHITE, BLACK, SCORE, LIVES, SIZE, FPS
from game_objects.paddle import Paddle
from game_objects.ball import Ball
from game_objects.life import Life


def main():
    pygame.init()
    pygame.display.set_caption("Mongoball")
    screen = pygame.display.set_mode(SIZE)
    paddle = Paddle()
    ball = Ball()
    sprite_group = pygame.sprite.Group()
    sprite_group.add(paddle)
    sprite_group.add(ball)
    life_sprite_group = pygame.sprite.Group()
    clock = pygame.time.Clock()

    current_lives = LIVES

    mouse_controlled = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse_x, _ = pygame.mouse.get_rel()

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] and not ball.moving:
            ball.toggle_moving()

        if mouse_x > 0:
            paddle.move_right(mouse_x)
            if not ball.moving:
                ball.move_with_paddle(paddle)
        else:
            paddle.move_left(abs(mouse_x))
            if not ball.moving:
                ball.move_with_paddle(paddle)

        if ball.rect.x >= 791:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 1:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > 599:
            sprite_group.remove(ball)
            ball = Ball()
            sprite_group.add(ball)
            current_lives -= 1
            life_sprite_group.spritedict.clear()

            if current_lives == 0:
                pygame.quit()
                quit()
        if ball.rect.y < 9:
            ball.velocity[1] = -ball.velocity[1]

        if pygame.sprite.collide_mask(ball, paddle):
            ball.paddle_bounce(paddle)

        for x in range(current_lives):
            life = Life(20 * (x + 1))
            life_sprite_group.add(life)

        sprite_group.update()
        life_sprite_group.update()
        screen.fill(BLACK)
        sprite_group.draw(screen)
        life_sprite_group.draw(screen)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
