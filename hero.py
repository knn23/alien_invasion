import pygame


class Hero:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship_png.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.speed_factor = 2.5

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed_factor
