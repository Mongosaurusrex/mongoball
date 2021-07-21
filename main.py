import pygame

from common.constants import WHITE, BLACK, SCORE, LIVES, SIZE, FPS
from game_objects.paddle import Paddle
from game_objects.ball import Ball
from game_objects.life import Life
from game_objects.brick import RedBrick


def main():
    pygame.init()
    pygame.display.set_caption("Mongoball")
    screen = pygame.display.set_mode(SIZE)

    persistent_sprite_group = pygame.sprite.Group()
    life_sprite_group = pygame.sprite.Group()
    level_sprite_group = pygame.sprite.Group()

    paddle = Paddle()
    ball = Ball(persistent_sprite_group)
    persistent_sprite_group.add(paddle)
    persistent_sprite_group.add(ball)

    #  TODO: Remove and add proper level handling
    for x in range(20):
        brick = RedBrick(x * 40, 40)
        level_sprite_group.add(brick)

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

        if ball.rect.x >= 800:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > 600:
            persistent_sprite_group.remove(ball)
            ball = Ball(persistent_sprite_group)
            persistent_sprite_group.add(ball)
            current_lives -= 1
            life_sprite_group.spritedict.clear()

            if current_lives == -1:
                pygame.quit()
                quit()
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        if pygame.sprite.collide_mask(ball, paddle):
            ball.paddle_bounce(paddle)

        brick_hit = pygame.sprite.spritecollide(ball, level_sprite_group, False)
        if brick_hit:
            hit_rect = brick_hit[0].rect
            if hit_rect.left > ball.rect.left or ball.rect.right < hit_rect.right:
                ball.velocity[0] = -ball.velocity[0]
                brick_hit[0].destroy()
            else:
                ball.velocity[1] = -ball.velocity[1]
                brick_hit[0].destroy()

        for x in range(current_lives):
            life = Life(20 * (x + 1))
            life_sprite_group.add(life)

        persistent_sprite_group.update()
        life_sprite_group.update()
        level_sprite_group.update()
        screen.fill(BLACK)
        persistent_sprite_group.draw(screen)
        life_sprite_group.draw(screen)
        level_sprite_group.draw(screen)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
