# game_over_menu.py
import pygame

class GameOverMenu:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('font/press-start-2p-regular.ttf', 48)  # Заголовок
        self.button_font = pygame.font.Font('font/press-start-2p-regular.ttf', 20)  # Шрифт для кнопок

        # Кнопки
        self.play_button = pygame.Rect(400, 300, 200, 40)  # Кнопка "Играть снова"
        self.exit_button = pygame.Rect(400, 360, 200, 40)  # Кнопка "Выход"
        self.score = 0

    def draw_menu(self):
        self.screen.fill((0, 0, 0))  # Чёрный фон
        title_image = self.font.render("Game Over", True, self.text_color)
        title_rect = title_image.get_rect(center=(500, 100))
        self.screen.blit(title_image, title_rect)

        score_text = self.button_font.render(f'Score: {self.score}', True, self.text_color)
        self.screen.blit(score_text, (400, 200))  # Положение текста счета

        mouse_pos = pygame.mouse.get_pos()

        # Изменяем цвет текста кнопки при наведении
        play_text_color = (255, 255, 0) if self.play_button.collidepoint(mouse_pos) else self.text_color
        exit_text_color = (255, 255, 0) if self.exit_button.collidepoint(mouse_pos) else self.text_color

        play_text = self.button_font.render("Play Again", True, play_text_color)
        self.screen.blit(play_text, (self.play_button.centerx - play_text.get_width() // 2,
                                      self.play_button.centery - play_text.get_height() // 2))

        exit_text = self.button_font.render("Exit", True, exit_text_color)
        self.screen.blit(exit_text, (self.exit_button.centerx - exit_text.get_width() // 2,
                                      self.exit_button.centery - exit_text.get_height() // 2))

        pygame.display.flip()

    def check_button_clicks(self, mouse_pos):
        if self.play_button.collidepoint(mouse_pos):
            return "play_again"
        elif self.exit_button.collidepoint(mouse_pos):
            return "exit"
        return None

    def set_score(self, score):
        self.score = score
