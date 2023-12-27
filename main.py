# main.py

import pygame
from game_module import main as game_main

def main():
    pygame.init()

    pygame.display.set_caption("Duck On The Run!")

    WIDTH, HEIGHT = (1600, 1000)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    game_main(screen)

    pygame.quit()

if __name__ == "__main__":
    main()
