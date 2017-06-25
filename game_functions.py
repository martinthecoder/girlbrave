import sys

import pygame

def check_keydown_events (event, girl):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        girl.moving_right = True
    elif event.key == pygame.K_LEFT:
        girl.moving_left = True

def check_keyup_events (event, girl):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        girl.moving_right = False
    elif event.key == pygame.K_LEFT:
        girl.moving_left = False

    
def check_events(girl):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events (event, girl)
        elif event.type == pygame.KEYUP:
            check_keyup_events (event, girl)

def update_screen (gb_settings, screen, girl):
    """Update images on the screen and flip to the new screen."""
    #Redraw the screen during each pass through the loop.
    screen.fill(gb_settings.bg_color)
    girl.blitme()

    #Make the most recently drawn screen visible.
    pygame.display.flip()
