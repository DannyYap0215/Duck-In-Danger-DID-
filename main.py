import pygame
import spritesheet 
from sys import exit

pygame.init()

#Game Name
pygame.display.set_caption("Duck On The Run!")

#fps,sizing
FPS = 60
WIDTH , HEIGHT = (1000,800)
BLACK = (0,0,0)
screen = pygame.display.set_mode((WIDTH , HEIGHT))

#for backgroud
#might impliment a moving background
background_surface = pygame.image.load("graphics/bg.png")

#for duck
duck_sprite_sheet_image = pygame.image.load("graphics/white-duck/white-duck-walk.png").convert_alpha()
#means sprite_sheet runs through the module"duck.py" and run through the class "DuckSpriteSheet" and run through the variable "duck_sprite_sheet_image"
sprite_sheet = spritesheet.SpriteSheet(duck_sprite_sheet_image)

#animation list for the ducks
animation_list = []
animation_steps = [3, 5]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 150
frame = 0
step_counter = 0

#loops animation in the animation step list, creates an empty list, 
#and for _ it loops through the animation which had looped throught the animation_step list ,
#getting _ images that had looped through and adding each to the temporary image list !
#after that, it loops through the second value in the list which will be 5
for animation in animation_steps:
    temp_image_list = []
    for _ in range(animation) :
        temp_image_list.append(sprite_sheet.get_image(step_counter , 40 , 40 , 5 , BLACK)) #add to list
        step_counter = step_counter + 1
    animation_list.append(temp_image_list)

def main(screen) :
    global frame,last_update
    clock = pygame.time.Clock()

    run = True
    while run :
        global action
        clock.tick(FPS)

        screen.blit(background_surface,(0,0))
        
        #update animation
        current_time = pygame.time.get_ticks( )
        if (current_time - last_update )>= animation_cooldown :
            frame = frame + 1
            last_update = current_time
            if frame >= len(animation_list[action]): #keeps looping the animation through the action 0,1,2
                frame = 0
       
        
        #from animation list, it goes through action, then access the frames from it
        screen.blit(animation_list[action][frame],(0,0))
        
        
    
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and action > 0:
                    action = action - 1
                    frame = 0
                elif event.key == pygame.K_UP and action < len(animation_list) - 1:
                    action = action + 1
                    frame = 0
        
    pygame.quit()
    quit()

if __name__ == "__main__" :
    main(screen)

