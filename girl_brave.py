import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from gamestats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #Initialize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings ()
    screen = pygame.display.set_mode (
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption ('Girl Brave')

    #Create instances to store game statistics and to create a scoreboard.
    stats = GameStats (ai_settings)
    sb = Scoreboard (ai_settings, screen, stats)

    #Make a ship, a group for bullets and a group for rapests
    ship = Ship (ai_settings, screen)
    alien = Alien (ai_settings, screen)
    bullets = Group ()
    aliens = Group ()

    #Create the fleet of rapests.
    gf.create_fleet (ai_settings, screen, ship, aliens)

    #Make the play button
    play_button = Button (ai_settings, screen, "Play")

    #Start the main loop for the game.
    while True:
        gf.check_events (ai_settings, screen, stats, play_button, ship, aliens,
                         bullets, sb)
        if stats.game_active == True:
            ship.update ()
            gf.update_bullets (ai_settings, screen, stats, sb, ship, aliens,
                               bullets)
            gf.update_aliens (ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_screen (ai_settings, screen, stats, sb, ship, aliens, bullets,
                              play_button)
run_game ()
        
