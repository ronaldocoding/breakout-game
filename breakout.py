import pygame
from Brick import Brick
from Ball import Ball
from Paddle import Paddle

pygame.init()

WIDTH = 893
HEIGHT = 780
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
GREY = (212, 210, 212)
BLACK = (0, 0, 0)
BLUE = (0, 97, 148)

RED = (162, 8, 0)
ORANGE = (183, 119, 0)
GREEN = (0, 127, 33)
YELLOW = (197, 199, 37)

score = 0
balls = 1
velocity = 4

paddle_width = 54
paddle_height = 20

all_sprites_list = pygame.sprite.Group()

ball = Ball(WHITE, 10, 10, velocity)
ball.rect.x = WIDTH // 2 - 5
ball.rect.y = HEIGHT // 2 - 5
    
# creating paddle
paddle = Paddle(BLUE, paddle_width, paddle_height)
paddle.rect.x = WIDTH // 2 - paddle_width // 2
paddle.rect.y = HEIGHT - 65

all_bricks = pygame.sprite.Group()

brick_width = 55
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 16


# bricks collors 
def bricks():
    for j in range(8):
        for i in range(14):
            if j < 2:
                if i == 0:
                    brick = Brick(RED, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(RED, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 1 < j < 4:
                if i == 0:
                    brick = Brick(ORANGE, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(ORANGE, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 3 < j < 6:
                if i == 0:
                    brick = Brick(GREEN, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(GREEN, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 5 < j < 8: 
                if i == 0:
                    brick = Brick(YELLOW, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(YELLOW, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
    return True


brick_wall = bricks()

all_sprites_list.add(paddle)
all_sprites_list.add(ball)


def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move_left(10, wall_width)
        if keys[pygame.K_RIGHT]:
            paddle.move_right(10, WIDTH, wall_width, paddle_width)

        all_sprites_list.update()

        if ball.rect.y < 40:
            ball.velocity[1] = -ball.velocity[1]

        if ball.rect.x >= WIDTH - wall_width - 10:
            ball.velocity[0] = -ball.velocity[0]

        if ball.rect.x <= wall_width:
            ball.velocity[0] = -ball.velocity[0]

        if ball.rect.y > HEIGHT:
            ball.rect.x = WIDTH // 2 - 5
            ball.rect.y = HEIGHT // 2 - 5
            ball.velocity[1] = ball.velocity[1]

        screen.fill(BLACK)

        # wall collors 
        pygame.draw.line(screen, GREY, [0, 19], [WIDTH, 19], 40)
        pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
        pygame.draw.line(screen, GREY, [(WIDTH - wall_width / 2) - 1, 0], [(WIDTH - wall_width / 2) - 1, HEIGHT],
                         wall_width)

        pygame.draw.line(screen, BLUE, [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
                         [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)
        pygame.draw.line(screen, BLUE, [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
                         [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)

        pygame.draw.line(screen, RED, [(wall_width / 2) - 1, 212.5], [(wall_width / 2) - 1, 212.5 + 2 *
                                                                      brick_height + 2 * y_gap], wall_width)
        pygame.draw.line(screen, RED, [(WIDTH - wall_width / 2) - 1, 212.5], [(WIDTH - wall_width / 2) - 1, 212.5 +
                                                                              2 * brick_height + 2 * y_gap], wall_width)

        pygame.draw.line(screen, ORANGE, [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
                         [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], wall_width)
        pygame.draw.line(screen, ORANGE, [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
                         [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], wall_width)

        pygame.draw.line(screen, GREEN, [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
                         [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], wall_width)
        pygame.draw.line(screen, GREEN, [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
                         [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], wall_width)

        pygame.draw.line(screen, YELLOW, [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
                         [(wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap], wall_width)
        pygame.draw.line(screen, YELLOW, [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
                         [(WIDTH - wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap], wall_width)

        # text score
        font = pygame.font.Font('DSEG14Classic-Bold.ttf', 70)
        text = font.render(str(f"{score:03}"), 1, WHITE)
        screen.blit(text, (80, 120))
        text = font.render(str(balls), 1, WHITE)
        screen.blit(text, (520, 41))
        text = font.render('000', 1, WHITE)
        screen.blit(text, (580, 120))
        text = font.render('1', 1, WHITE)
        screen.blit(text, (20, 40))

        all_sprites_list.draw(screen)

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()


main()
