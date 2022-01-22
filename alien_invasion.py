import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
import os

def run_game() -> None:
    x = 300
    y = 100
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_height, ai_settings.screen_width))
    ship = Ship(ai_settings, screen)
    pygame.display.set_caption('Alien Invasion')
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


if __name__ == '__main__':
    run_game()
