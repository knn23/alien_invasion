import pygame
from pygame.sprite import Sprite


class AlienBullet(Sprite):
    def __init__(self, settings, screen, alien):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 15)  # Размер пули пришельца
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom
        self.color = settings.alien_bullet_color
        self.speed_factor = settings.alien_bullet_speed

    def update(self):
        self.rect.y += self.speed_factor

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
