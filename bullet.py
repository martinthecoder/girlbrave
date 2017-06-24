import pygame
from pygame.sprite import Sprite


class Bullet (Sprite):
    """A class to manage bullets fired from the girl."""

    def __init__(self, gb_settings, screen, girl):
        """Create a bullet object at the girl's current position."""
        super (Bullet, self).__init__()
        self.screen = screen

        #Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0,0, gb_settings.bullet_width, gb_settings.bullet_height)
        self.rect.centerx = girl.rect.centerx
        self.rect.top = girl.rect.top

        #Store the bullet's position as a decimal value.
        self.y = float (self.rect.y)

        self.color = gb_settings.bullet_color
        self.speed_factor = gb_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        #Update the decimal position of the bullet.
        self.y -= self.speed_factor
        #Update the rect position.
        self.rect.y = self.y

    def draw_bullet (self):
        """Draw the bullet to the screen."""
        pygame.draw.rect (self.screen, self.color, self.rect)
                                 
