class Settings:
    def __init__(self):
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = [255, 0, 0]
        self.alien_bullet_color = [0, 255, 0]
        self.alien_bullet_speed = 2
        self.alien_speed_factor = 1.3
        self.alien_fire_rate = 300  # Частота выстрелов пришельцев (0.5 секунды)
        self.bg_color = (10, 10, 40)
