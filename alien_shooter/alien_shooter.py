# GAME IS CREATED BY ANANT NARAYAN PATEL
# COPYING ANY PART OF CODE IS STRICTLY PROHIBITED

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # initializing the game and creating the screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Shooter -- created by || ANANT ||")
    # Make the play button.
    play_button = Button(settings, screen, "Play || ANANT")
    # Create an instance to store game statistics.
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    # making a ship
    ship = Ship(settings, screen)
    # make a group to store bullets in
    bullets = Group()
    aliens = Group()
    # create a fleet of aliens.
    gf.create_fleet(settings, screen, ship, aliens)

    # start the main loop of the game
    while True:
        gf.check_events(settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(settings, stats, screen, ship, aliens, bullets)
            print("Designed by || ANANT ||")
        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
