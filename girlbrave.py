
import pygame
from settings import Settings
from girl import Girl
import game_functions as gf

def run_game ():
    #Initialize game and create a screen object
    pygame.init()
    gb_settings = Settings()
    screen = pygame.display.set_mode (
        (gb_settings.screen_width, gb_settings.screen_height))
    pygame.display.set_caption ("Girl Brave")

    #Make a girl
    girl = Girl (screen)

    #Set the background color.
    bg_color = (230, 230, 230)

    #Start the main loop for the game.
    while True:
        gf.check_events (girl)
        girl.update()
        gf.update_screen(gb_settings, screen, girl)

        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Redraw the screen during each pass through the loop.
        screen.fill (gb_settings.bg_color)
        girl.blitme()

        #Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
