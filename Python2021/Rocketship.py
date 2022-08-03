import pygame

class Rocketship:
    """A class to manage the rocket"""

    def __init__(self, rk_game):
        """Initialize the rocket and set its starting position"""
        self.screen = rk_game.screen
        self.settings = rk_game.settings
        self.screen_rect = rk_game.screen.get_rect()

        # Load the rocket image and get its rect.
        self.image = pygame.image.load("C:/Users/Carlito/Desktop/rocket.bmp")
        self.rect = self.image.get_rect()

        # location of the rocket
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the ships horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket based on the movment flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket at the location"""
        self.screen.blit(self.image, self.rect)