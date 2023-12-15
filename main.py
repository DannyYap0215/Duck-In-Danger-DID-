import pygame
import spritesheet 
from sys import exit

pygame.init()

#Game Name
pygame.display.set_caption("Duck On The Run!")

#fps,sizing
FPS = 60
WIDTH , HEIGHT = (1600,1000)
BLACK = (0,0,0)
screen = pygame.display.set_mode((WIDTH , HEIGHT))

#for backgroud
#might impliment a moving background
background_surface = pygame.image.load("graphics/bg.png")

#for duck
duck_sprite_sheet_image = pygame.image.load("graphics/white-duck/white-duck-walk.png").convert_alpha()
#means sprite_sheet runs through the module"duck.py" and run through the class "DuckSpriteSheet" and run through the variable "duck_sprite_sheet_image"
sprite_sheet = spritesheet.DuckSpriteSheet(duck_sprite_sheet_image)
white_duck_frame_0 = sprite_sheet.get_image(0 , 40 , 40 , 2.5 , BLACK)
white_duck_frame_1 = sprite_sheet.get_image(1 , 40 , 40 , 2.5 , BLACK)
white_duck_frame_2 = sprite_sheet.get_image(2 , 40 , 40 , 2.5 , BLACK)
white_duck_frame_3 = sprite_sheet.get_image(3 , 40 , 40 , 2.5 , BLACK)
white_duck_frame_4 = sprite_sheet.get_image(4 , 40 , 40 , 2.5 , BLACK)
white_duck_frame_5 = sprite_sheet.get_image(5 , 40 , 40 , 2.5 , BLACK)

def main(screen) :
    clock = pygame.time.Clock()

    run = True
    while run :
        clock.tick(FPS)

        screen.blit(background_surface,(0,0))
        
        screen.blit(white_duck_frame_0,(0,0))
        screen.blit(white_duck_frame_1,(200,0))
        screen.blit(white_duck_frame_2,(400,0))
        screen.blit(white_duck_frame_3,(600,0))
        screen.blit(white_duck_frame_4,(800,0))
        screen.blit(white_duck_frame_5,(1000,0))
        
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False
                break
    
    pygame.quit()
    quit()

if __name__ == "__main__" :
    main(screen)

