class SideSettings:

    def __init__(self):
        """Initialize the game settings"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230 ,230)

        # SpaceShip settings
        self.spaceship_speed = .5

        # Bullet settings
        self.bullet_speed = .75
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
