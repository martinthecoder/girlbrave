

class Settings ():
    """A class to store all settings for Girl Brave."""

    def __init__ (self):
        """Initialize the game settings."""
        #Screen settings.
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (252, 40, 71)

        #Girl settings
        self.girl_speed_factor = 1

        #Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
