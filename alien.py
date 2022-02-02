import pygame
from pygame.sprite import Sprite

ALIEN_ICO = 'alien.bmp'


class Alien(Sprite):
    """A class to represents a singly alien in the fleet"""

    def __init__(self, ai_settings: object, screen: object) -> None:
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(ALIEN_ICO)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if an alien is at edge of screen"""
        scree_rect = self.screen.get_rect()
        if self.rect.right >= scree_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
