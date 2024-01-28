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

# *********************************************************
# Program: main.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL9L
# Year: 2023/24 Trimester 1
# Names: YAP CHI YI | THAM MEI TING | TAN YONG XIN
# IDs: 1221106350 | 1221106865 | 1221106569
# Emails: 1221106350@student.mmu.edu.my | 1221106865@student.mmu.edu.my | 1221106569@student.mmu.edu.my
# Phones: 018-2694514 | 017-3268006 | 012-6556505
# *********************************************************

