import sys
import pygame
from bullet import Bullet
from settings import Settings

def check_keydown_events (event, gb_settings, screen, girl, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        girl.moving_right = True
    elif event.key == pygame.K_LEFT:
        girl.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Create a new bullet and add it to the bullets group.
        new_bullet = Bullet (gb_settings, screen, girl)
        bullets.add(new_bullet)

def check_keyup_events (event, girl):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        girl.moving_right = False
    elif event.key == pygame.K_LEFT:
        girl.moving_left = False
        
def check_events(gb_settings, screen, girl, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events (event, gb_settings, screen, girl, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events (event, girl)
    
def update_screen (gb_settings, screen, girl, bullets):
    """Update images on the screen and flip to the new screen."""
    #Redraw the screen during each pass through the loop.
    for bullet in bullets.sprites ():
        bullet.draw_bullet()
    screen.fill (gb_settings.bg_color)
    girl.blitme()

    #Make the most recently drawn screen visible.
    pygame.display.flip()
