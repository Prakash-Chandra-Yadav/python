import sys 
import pygame 
from settings import Settings
from ship import Ship

class AlienInvasion:
    '''overall class to manage the game assets and behaviors'''
    def __init__(self):
        '''initialize the game and create the game resources'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("ALIEN INVASION")
        self.ship = Ship(self)

        #set the background color
        self.bg_color = (230,230,230)
    def run_game(self):
        '''start the main loop for the game'''
        while True: 
            #watch for the keyboard respoisne and events 
            self._check_events()
            ##controls the ship movements 
            self.ship.update()
            #redraw the screen during each pass through the loop
            self._update_screen()
            self.clock.tick(60)
    def _check_events(self):
        '''responds to the keypress and mouse events'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        '''respond to key presses'''
        if event.key == pygame.K_RIGHT:
        ##move the ship to the right 
            self.ship.moving_right = True 
        elif event.key == pygame.K_LEFT:
        #move the ship to the left 
            self.ship.moving_left = True
    def _check_keyup_events(self,event):
        '''respond to the key releases'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def _update_screen(self):
        '''updates the image on the screen and flip to the new screen'''
         #redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #make most recently drawn screen visible 
        pygame.display.flip()


if __name__ == '__main__':
    #make the game instance and run the game 
    ai = AlienInvasion()
    ai.run_game()