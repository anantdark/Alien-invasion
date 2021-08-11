class GameStats():
    """ Track statistics for Alien Invasion"""

    def __init__(self, settings):
        """ Initialize statistics."""
        self.settings = settings
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = False

        self.high_score = 0

    def reset_stats(self):
        """ Initialize statistics that can change during the gmae"""
        self.ships_left = self.settings.ship_limit
        self.score = 0