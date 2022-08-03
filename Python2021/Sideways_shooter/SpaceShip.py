import pygame

class SpaceShip:

    def __init__(self, ss_game):
        """Initialize the ship and set its starting position"""
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load("C:/Users/Carlito/Desktop/spaceship3.png")
        self.rect = self.image.get_rect()

        # Position of SpaceShip
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ships vertical position
        self.y = float(self.rect.y)
    
        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ships position based on the movement flag"""
        # Update the ships y value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.spaceship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.spaceship_speed

        # Update rect object from self.y
        self.rect.y = self.y

    def bliteme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)