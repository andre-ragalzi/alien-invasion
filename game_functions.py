
from os import stat
import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet


def change_fleet_direction(ai_settings: object, aliens: object) -> None:
    """Drop th entire fleet and change the fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings: object, aliens: object) -> None:
    """Respond appropriately if any aliens have reached edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_keydown_events(event: object, ai_settings: object, screen: object, ship: object, bullets: object) -> None:
    """Respond to keypress."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event: object, ship: object) -> None:
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_bullet_alien_collisions(ai_settings: object, screen: object, ship: object, aliens: object, bullets: object) -> None:
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def check_events(ai_settings: object, screen: object, ship: object, bullets: object) -> None:
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.QUIT:
            pygame.quit()


def create_alien(ai_settings: object, screen: object, aliens: object, alien_number: object, row_number: object) -> None:
    """Create an alien and place it in a row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def check_aliens_bottom(ai_settings: object, stats: object, screen: object, ship: object,
                        aliens: object, bullets: object) -> None:
    """Check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)


def create_fleet(ai_settings: object, screen: object, ship: object, aliens: object) -> None:
    """Create a flull fleets of aliens"""
    alien = Alien(ai_settings, screen)
    numbers_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(numbers_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings: object, alien_width: object) -> None:
    """Determine tte number of aliens that fit in a row"""
    avalaible_space_x = ai_settings.screen_width - 2 * alien_width
    numbers_aliens_x = int(avalaible_space_x / (2*alien_width))
    return numbers_aliens_x


def get_number_rows(ai_settings: object, ship_height: int, alien_height: int) -> None:
    """Determine the number of rows of aliens that fit on the screen"""
    avalaible_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(avalaible_space_y / (2*alien_height))
    return number_rows


def update_aliens(ai_settings: object, stats: object, screen: object, ship: object, aliens: object, bullets: object) -> None:
    """Update the positions fo all aliens in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)


def update_screen(ai_settings: object, screen: object, ship: object, aliens: object, bullets: object) -> None:
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(ai_settings: object, screen: object, ship: object, aliens: object, bullets: object) -> None:
    """Update position of bullets and get rid of old bullets"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def fire_bullet(ai_settings: object, screen: object, ship: object, bullets: object) -> None:
    """Fire a bullet if limit not reached yet"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def ship_hit(ai_settings: object, stats: object, screen: object, ship: object, aliens: object, bullets: object) -> None:
    """Respond to ship being hit by alien"""
    if stats.ship_left > 0:
        stats.ship_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False


if __name__ == '__main__':
    pass
