
import pygame

ICO_SPACE_SHIP = 'space_ship.bmp'


class Ship:
    def __init__(
            self, ai_settings: object, screen: object) -> None:
        """Initialize the ship image and get its rect."""
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(ICO_SPACE_SHIP)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def blitme(self) -> None:
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx

    def update(self) -> None:
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center


if __name__ == '__main__':
    pass
