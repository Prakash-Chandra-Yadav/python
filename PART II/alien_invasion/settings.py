class Settings: 
    '''a class to store all the settings for the alien invasion'''
    def __init__(self):
        '''initialize the game settings'''
        #screen settings 
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230,230,230)
        self.ship_speed = 2

        #bullet settings 
        self.bullet_speed = 2.5
        self.bullet_width = 300
        self.bullet_height =15 
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3

        #alien settings 
        self.alien_speed = 1.0 
        self.fleet_drop_speed = 10 
        #fleet direction of 1 represent right; -1 represeng left 
        self.fleet_dircetion = 1



