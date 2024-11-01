import pygame
import sys
import random
from pygame.sprite import Group
from settings import Settings
from statistics import Statistic
from hero import Hero
from bullet import Bullet
from alien import Alien
from alien_bullet import AlienBullet
from menu import Menu
from game_over_menu import GameOverMenu

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen_width = 1000
        self.screen_height = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.hero = Hero(self.screen)
        self.bullets = Group()
        self.aliens = Group()
        self.game_over_menu = GameOverMenu(self)
        self.alien_bullets = Group()
        self.stats = Statistic(self)
        self.last_alien_fire_time = 0
        self.last_alien_fire_index = 0
        self.menu = Menu(self)
        self._game_active = False
        self._create_alien()

    def run_game(self):
        while True:
            if not self._game_active:
                self._check_menu_events()
                self.menu.draw_menu()
            elif self.stats.health <= 0:
                self.game_over_menu.draw_menu()
            else:
                self._check_events()
                self.hero.update()
                self._update_bullets()
                self._update_aliens()
                self._update_alien_bullets()
                self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.hero.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.hero.moving_left = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.hero.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.hero.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.aliens.draw(self.screen)
        self.hero.blitme()
        self.draw_star()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for alien_bullet in self.alien_bullets.sprites():
            alien_bullet.draw_bullet()

        self.stats.show_score()
        self.stats.show_health()
        pygame.display.flip()

    def draw_star(self, num_star=100):
        for _ in range(num_star):
            x = random.randint(0, self.screen_width)
            y = random.randint(0, self.screen_height)
            self.screen.fill((255, 255, 255), (x, y, 2, 2))

    def _check_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                action = self.menu.check_button_clicks(mouse_pos)
                if action == "play":
                    self._start_game()
                elif action == "exit":
                    pygame.quit()
                    sys.exit()

    def _start_game(self):
        self._game_active = True
        pygame.time.delay(0)
        self._create_alien()

    def _create_alien(self):
        alien = Alien(self.settings, self.screen)
        alien.rect.x = random.randint(0, self.screen_width - alien.rect.width)
        alien.rect.y = -alien.rect.height
        self.aliens.add(alien)

    def _update_aliens(self):
        self.aliens.update()
        for alien in self.aliens.copy():
            if alien.rect.top >= self.screen_height:
                self.aliens.remove(alien)

        if len(self.aliens) < 5 and random.randint(0, 100) < 2:
            self._create_alien()

        self._alien_fire_bullet()

    def _alien_fire_bullet(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_alien_fire_time > self.settings.alien_fire_rate:
            alien_list = list(self.aliens.sprites())
            if alien_list:
                if self.last_alien_fire_index < len(alien_list):
                    alien = alien_list[self.last_alien_fire_index]
                    alien_bullet = AlienBullet(self.settings, self.screen, alien)
                    self.alien_bullets.add(alien_bullet)
                    self.last_alien_fire_time = current_time
                    self.last_alien_fire_index += 1
                    if self.last_alien_fire_index >= len(alien_list):
                        self.last_alien_fire_index = 0

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            self.stats.ships_destroyed += len(collisions)
            self.stats.prep_score()

    def _update_alien_bullets(self):
        self.alien_bullets.update()
        for bullet in self.alien_bullets.copy():
            if bullet.rect.top >= self.screen_height:
                self.alien_bullets.remove(bullet)

        collisions = pygame.sprite.spritecollide(self.hero, self.alien_bullets, True)
        if collisions:
            self.stats.health -= 10
            print(f"Здоровье героя: {self.stats.health}")
            self.stats.prep_health()
            if self.stats.health <= 0:
                print("Игра окончена! Здоровье героя закончилось.")
                pygame.quit()
                sys.exit()

    def _fire_bullet(self):
        if len(self.bullets) < 5:
            new_bullet = Bullet(self.screen, self.settings, self.hero)
            self.bullets.add(new_bullet)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
