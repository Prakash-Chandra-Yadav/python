import pygame 
import settings
class Ship: 
    '''a class to manage the ship'''
    def __init__(self,ai_game):
        '''initialize the ship and set its starting position'''
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings 

        ##load the ship image and get its rect 
        self.image =pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        ##start each new ship at the buttom center of the screen 
        self.rect.midbottom = self.screen_rect.midbottom 

        #store a float for the ships exact horizontal position 
        self.x = float(self.rect.x)


        #movement flag; start with a ship that is not moving 
        self.moving_right = False
        self.moving_left = False
    def update(self):
        '''updates the ships position based on the movement flag'''
        #update the x calue not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed 
        if self.moving_left and self.rect.left >0:
            self.x -= self.settings.ship_speed
        #update the object from self.x
        self.rect.x = self.x
    def blitme(self):
        '''draw the ship at its current location'''
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        '''center the shipnon the screen'''
        self.rect.midbottom = self.screen_rect.midbottom 
        self.x = float(self.rect.x)