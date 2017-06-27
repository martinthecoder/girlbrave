import pygame

class GameStats():
    """Track statistics for Girl Brave."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        #Start Girl Brave in an inactive state
        self.game_active = False
        #Load hugh score from file.
        with open ('high_score.txt') as file_object:
            self.high_score = int(file_object.read())

    def reset_stats(self):
        """
        Initialise statistics that change throughout the game and are reset
        each time a new game is started.
        """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
