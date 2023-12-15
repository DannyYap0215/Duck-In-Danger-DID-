import pygame
import duck 
from sys import exit

pygame.init()

#Game Name
pygame.display.set_caption("Duck On The Run!")

#fps,sizing
FPS = 60
WIDTH , HEIGHT = (1200,800)
BLACK = (0,0,0)
screen = pygame.display.set_mode((WIDTH , HEIGHT))

#for backgroud
#might impliment a moving background
background_surface = pygame.image.load("graphics/bg.png")

#for duck
duck_sprite_sheet_image = pygame.image.load("graphics/duck.png").convert_alpha()
#means sprite_sheet runs through the module"duck.py" and run through the class "DuckSpriteSheet" and run through the variable "duck_sprite_sheet_image"
sprite_sheet = duck.DuckSpriteSheet(duck_sprite_sheet_image)
duck_frame_0 = sprite_sheet.get_image(0 , 40 , 40 , 3 , BLACK)



def main(screen) :
    clock = pygame.time.Clock()

    run = True
    while run :
        clock.tick(FPS)

        screen.blit(background_surface,(0,0))
        screen.blit(duck_frame_0,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False
                break
    
    pygame.quit()
    quit()

if __name__ == "__main__" :
    main(screen)

