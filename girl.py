import pygame

class Girl():

    def __init__(self, gb_settings, screen):
        """Initialize the girl and set its starting position."""
        self.screen = screen
        self.gb_settings = gb_settings

        #Load the girl image and get its rect.
        self.image = pygame.image.load ('images/girl.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new girl at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the girl's center.
        self.center = float (self.rect.centerx)
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update (self):
        """Update the girl's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.gb_settings.girl_speed_factor
            #self.rect.centerx += 10
        if self.moving_left and self.rect.left :
            self.center -= self.gb_settings.girl_speed_factor
            #self.rect.centerx -= 10
        #Update rect object from self.center.
        self.rect.centerx = self.center
    def blitme(self):
        """Draw the girl at its current position."""
        self.screen.blit (self.image, self.rect)
