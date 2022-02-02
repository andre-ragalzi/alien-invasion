class GameStats:
    """Track statistics for Alien Invasion"""
    def __init__(self, ai_settings: object)->None:
        self.ai_settings = ai_settings
        self.game_active = True
        self.reset_stats()
    def reset_stats(self):
        """Initializa the statistics the can change during the game"""
        self.ship_left = self.ai_settings.ship_limit