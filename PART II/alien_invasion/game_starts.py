class GameStarts:
    '''track the stastitics of the alien invasion'''
    def __init__(self,ai_game):
        self.settings = ai_game.settings 
        self.reset_stats()
    def reset_starts(self):
        '''initialize the stastitics that can change during the game'''
        self.ships_left = self.settings.ship_limit