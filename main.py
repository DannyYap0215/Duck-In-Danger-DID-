# main.py
import pygame
from sys import exit
from game_module import main as game_main #import main(screen) from the game_module.py 

pygame.init()

pygame.display.set_caption("Duck On The Run!")

FPS = 60
WIDTH, HEIGHT = (1000, 800)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

if __name__ == "__main__":
    game_main(screen)
