import pygame
from sys import exit
from game_module import main as game_main 

pygame.init()

pygame.display.set_caption("Duck On The Run!")

FPS = 60
WIDTH, HEIGHT = (1600, 1000)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

if __name__ == "__main__":
    game_main(screen)
