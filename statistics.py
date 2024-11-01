import pygame


class Statistic:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        try:
            self.font = pygame.font.Font('font/press-start-2p-regular.ttf', 16)
        except FileNotFoundError:
            print("Шрифт не найден. Используется системный шрифт.")
            self.font = pygame.font.SysFont(None, 48)

        self.reset_stats()
        self.prep_score()
        self.prep_health()

    def reset_stats(self):
        self.ships_destroyed = 0
        self.health = 100  # Начальное здоровье героя

    def prep_score(self):
        score_str = f"Ships Destroyed: {self.ships_destroyed}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = 20
        self.score_rect.top = 20

    def prep_health(self):
        health_str = f"Health: {self.health}"
        self.health_image = self.font.render(health_str, True, self.text_color, self.settings.bg_color)
        self.health_rect = self.health_image.get_rect()
        self.health_rect.topright = (self.screen_rect.right - 20, 20)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)

    def show_health(self):
        self.screen.blit(self.health_image, self.health_rect)
