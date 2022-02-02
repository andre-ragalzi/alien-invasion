import os
import sys

import pygame
from pygame.sprite import Group

import game_functions as gf
from alien import Alien
from game_stats import GameStats
from settings import Settings
from ship import Ship


def run_game() -> None:
    x = 300
    y = 100
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_height, ai_settings.screen_width))
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    pygame.display.set_caption('Alien Invasion')
    stats = GameStats(ai_settings)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


if __name__ == '__main__':
    run_game()
