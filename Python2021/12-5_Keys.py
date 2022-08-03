import sys

import pygame
from pygame.constants import WINDOWHIDDEN

class Keys:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Keys")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.rect.x += 1

            pygame.display.flip()
            

if __name__ == "__main__":
    key = Keys()
    key.run_game()