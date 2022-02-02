class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self) -> None:
        self.bullet_speed_factor = 1
        self.bullet_width = 1
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        self.screen_width = 650
        self.screen_height = 650
        self.bg_color = (135, 206, 250)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1


if __name__ == '__main__':
    pass
