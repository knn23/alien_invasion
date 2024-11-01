import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/alien_png.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = settings.alien_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.speed
