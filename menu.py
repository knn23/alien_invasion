import pygame
import random


class Menu:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('font/press-start-2p-regular.ttf', 48)  # Заголовок
        self.button_font = pygame.font.Font('font/press-start-2p-regular.ttf', 20)  # Шрифт для кнопок

        # Кнопки
        self.play_button = pygame.Rect(400, 300, 200, 40)  # Высота кнопки уменьшена
        self.exit_button = pygame.Rect(400, 360, 200, 40)  # Расстояние между кнопками уменьшено

    def draw_menu(self):
        self.screen.fill(self.settings.bg_color)
        self._draw_stars()  # Добавим звезды на фон

        title_image = self.font.render("Alien Invasion", True, self.text_color)
        title_rect = title_image.get_rect(center=(500, 100))
        self.screen.blit(title_image, title_rect)

        mouse_pos = pygame.mouse.get_pos()

        # Изменяем цвет текста кнопки при наведении
        if self.play_button.collidepoint(mouse_pos):
            play_text_color = (255, 255, 0)  # Желтый цвет
        else:
            play_text_color = self.text_color

        if self.exit_button.collidepoint(mouse_pos):
            exit_text_color = (255, 255, 0)  # Желтый цвет
        else:
            exit_text_color = self.text_color

        # Отображаем текст кнопок с использованием меньшего шрифта
        play_text = self.button_font.render("Play", True, play_text_color)
        self.screen.blit(play_text, (self.play_button.centerx - play_text.get_width() // 2,
                                      self.play_button.centery - play_text.get_height() // 2))

        exit_text = self.button_font.render("Exit", True, exit_text_color)
        self.screen.blit(exit_text, (self.exit_button.centerx - exit_text.get_width() // 2,
                                      self.exit_button.centery - exit_text.get_height() // 2))

        pygame.display.flip()

    def _draw_stars(self, num_stars=100):
        for _ in range(num_stars):
            x = random.randint(0, self.screen.get_width())
            y = random.randint(0, self.screen.get_height())
            self.screen.fill((255, 255, 255), (x, y, 2, 2))  # Рисуем звезды

    def check_button_clicks(self, mouse_pos):
        if self.play_button.collidepoint(mouse_pos):
            return "play"
        elif self.exit_button.collidepoint(mouse_pos):
            return "exit"
        return None
