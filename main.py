import pygame
from sys import exit
pygame.init()


#Game Name
pygame.display.set_caption("Duck On The Run!")

#fps,sizing
FPS = 60
WIDTH , HEIGHT = (1200,800)

screen = pygame.display.set_mode((WIDTH , HEIGHT))


background_surface = pygame.image.load("graphics/bg.png")


# def background():
#     for i in range(WIDTH + 200) :
#         for j in range(100/height + 1) :



def main(screen) :
    clock = pygame.time.Clock()

    run = True
    while run :
        clock.tick(FPS)

        screen.blit(background_surface,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False
                break
    
    pygame.quit()
    quit()

if __name__ == "__main__" :
    main(screen)

