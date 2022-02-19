import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    # paddle moviment
    def move_right(self, pixels, window_width, wall_width, paddle_width):
        self.rect.x += pixels
        if self.rect.x > window_width - wall_width - paddle_width:
            self.rect.x = window_width - wall_width - paddle_width

    def move_left(self, pixels, wall_width):
        self.rect.x -= pixels
        if self.rect.x < wall_width:
            self.rect.x = wall_width
