class Settings ():
    """A class to store all settings for Girl Brave."""
#251 40 71
    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings
        self.screen_width = 1320 #1200
        self.screen_height = 700 #800
        self.bg_color = 255, 40, 71
        #Ship settings
        self.ship_limit = 3
        #Bullet settings
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #Button
        
        #Alien settings
        self.fleet_drop_speed = 10 #10
        #How quickly the game speeds up
        self.speedup_scale = 1.1 #1.1
        self.score_scale = 1.5

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings (self):
        """Initialise settings that change throughout the game."""
        self.ship_speed_factor = 1.5 #1.5 1.25
        self.bullet_speed_factor = 2 #3 2.5
        self.alien_speed_factor = 0.75 #1 0.75
        #Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_points = 50
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int (self.alien_points * self.score_scale)
        
