import sys

import pygame

from Bs_settings import Settings
from Bs_ship import Ship

class BlueSky:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Leeto's Game")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop of the game"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visibile
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    bs = BlueSky()
    bs.run_game()