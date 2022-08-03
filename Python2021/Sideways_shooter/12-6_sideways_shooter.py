import sys
import pygame

from SideSettings import SideSettings
from SpaceShip import SpaceShip
from Space_bullet import Bullet

class SidewayShooter:

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init() # initailize pygame
        self.settings = SideSettings() # uses the settings from the import

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # create a display window
        pygame.display.set_caption("Sideways Shooter") # Name in the window

        self.spaceship = SpaceShip(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.spaceship.update()
            self._update_bullets()
            self._update_screen()
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get(): # get events from a queue
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_UP:
            self.spaceship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.spaceship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_UP:
            self.spaceship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.spaceship.moving_down = False

    def _fire_bullet(self):
        """"Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.spaceship.bliteme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # make the most recently drawn screen visible
        pygame.display.flip() 

if __name__ == "__main__":
    # Make a game instance and run the game
    ss = SidewayShooter()
    ss.run_game()