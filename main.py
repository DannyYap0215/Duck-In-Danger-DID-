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

#animation list for white duck and brown duck
animation_list = []
animation_steps = 3
last_update = pygame.time.get_ticks()
animation_cooldown = 200
frame = 0

for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(x , 40 , 40 , 5 , BLACK)) #add to list


def main(screen) :
    global frame,last_update
    clock = pygame.time.Clock()

    run = True
    while run :
        clock.tick(FPS)

        screen.blit(background_surface,(0,0))
        
        #update animation
        current_time = pygame.time.get_ticks( )
        if (current_time - last_update )>= animation_cooldown :
            frame = frame + 1
            last_update = current_time
            if frame >= len(animation_list): #keeps looping the animation
                frame = 0
       
        
        
        screen.blit(animation_list[frame],(0,0))
        
        
    
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False
                break
    
    pygame.quit()
    quit()

if __name__ == "__main__" :
    main(screen)

