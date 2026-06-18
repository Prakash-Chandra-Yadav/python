import sys 
from time import sleep 
import pygame 
from settings import Settings
from game_starts import GameStarts
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from scoreboard import Scoreboard


class AlienInvasion:
    '''overall class to manage the game assets and behaviors'''
    def __init__(self):
        '''initialize the game and create the game resources'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("ALIEN INVASION")
        #create an instance to store the stastitics 
        self.stats = GameStarts(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        #set the background color
        self.bg_color = (230,230,230)

        #start the alien envasion in the active state 
        self.game_active = False

        #make the play button button 
        self.play_button = Button(self,"play")
    def run_game(self):
        '''start the main loop for the game'''
        while True: 
            #watch for the keyboard respoisne and events 
            self._check_events()
            if self.game_active:
                ##controls the ship movements 
                self.ship.update()
                ##update the bullets 
                self._update_bullets()
                #update the aliens
                self._update_aliens()
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_keydown_events(self,event):
        '''respond to key presses'''
        if event.key == pygame.K_RIGHT:
        ##move the ship to the right 
            self.ship.moving_right = True 
        elif event.key == pygame.K_LEFT:
        #move the ship to the left 
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        ##quit the game when user pressed the q button 
        elif event.key == pygame.K_q:
            sys.exit()
    def _check_keyup_events(self,event):
        '''respond to the key releases'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self, mosue_pos):
        '''start a new game when the player clicks play'''
        button_clicked = self.play_button.rect.collidepoint(mosue_pos)
        if button_clicked and not self.game_active:
            #reset the same settings
            self.settings.initialize_dynamic_settings()
            self.stats.reset_starts()
            self.game_active  = True
            #get rid of  any remaining bullets and aliens 
            self.bullets.empty()
            self.aliens.empty()

            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #hide the mouse button 
            pygame.mouse.set_visible(False)
        else: 
            self.game_active = False 
            pygame.mouse.set_visible(True)

    ##method that handles the fire of the bullet 
    def _fire_bullet(self):
        '''create the new bullet and add it to the bullet group'''
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _ship_hit(self):
        '''respond to the ship being hit by an alien'''
        if self.stats.ships_left > 0:
            #decrement the ship left 
            self.stats.ships_left -= 1

            #get rid of any remaining bullets and aliens 
            self.bullets.empty()
            self.aliens.empty()

            #create a new fleet and center the sheep 
            self._create_fleet()
            self.ship.center_ship()

            #pause 
            sleep(0.5)
        else: 
            self.game_active = False
    def _check_aliens_bottom(self):
        '''check if any aliens have reached the bottom of the screen'''
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #treat if same as the ship got hit 
                self._ship_hit()
                break
    def _update_bullets(self):
        '''update the position of the bullets and get rid of old bullets '''
        #update the bullet positions
                    #update the position of the bullet 
        self.bullets.update()

        #get rid of the bullet that have disappeared 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        #check for any bullets that have hit aliens
        #if so get rid of the bullet and the alien 
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens, True, True)
        if not self.aliens: 
            #distroy the existing bullet and create the new fleet 
            self.bullets.empty()
            self._create_fleet()
    def _check_bullet_alien_collisions(self):
                #check for any bullets that have hit aliens
        #if so get rid of the bullet and the alien 
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens, True, True)
        if not self.aliens: 
            #distroy the existing bullet and create the new fleet 
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
    def _update_aliens(self):
        '''update the position of all the aliens'''
        '''check if the fleet is at the edge then change the direction'''
        self._check_fleet_edges()
        self.aliens.update()
        #look if alien-ship collision 
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        #look for alien hitting the bottom of the screen 
        self._check_aliens_bottom()
    def _check_fleet_edges(self):
        '''respond appropriately if any of the alien has reached the edge'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        '''drop the entire fleet and change the fleet direction'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_dircetion *= -1
    def _create_fleet(self):
        '''create the fleet of the aliens'''
        #make an alien 
        #create the alien and keep adding aliens until theres no room left 
        #spacing between aliens is one alien width and one to the height  
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size 

        current_x,current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):  
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x,current_y)
                current_x += 2 * alien_width
            #finished a row, reset the x avlue and increment the y value
            current_x = alien_width
            current_y += 2 * alien_height
    def _create_alien(self,x_position,y_position):
        '''create an alien and place it in the row'''
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_screen(self):
        '''updates the image on the screen and flip to the new screen'''
         #redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        #draw the score information 
        self.sb.show_score()
        #draw the paly butto if the game is inactive 
        if not self.game_active:
            self.play_button.draw_button()
        #make most recently drawn screen visible 
        pygame.display.flip()


if __name__ == '__main__':
    #make the game instance and run the game 
    ai = AlienInvasion()
    ai.run_game()