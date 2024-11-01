import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen, ai_settings, hero):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = hero.rect.centerx
        self.rect.top = hero.rect.top
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.rect.y -= self.speed_factor

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
