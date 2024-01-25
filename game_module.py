import pygame
from animation import AnimationController
import math
import random
import spritesheet
#remember to add Duck in Danger/ to each path when submitting as a ZIP file

def start_button(screen):
    start_button_rect = pygame.Rect(740, 350, 200, 100)
    pygame.draw.rect(screen, (0, 0, 0), start_button_rect)
    font_size = 72
    font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render("Start", True, (255, 255, 255))
    text_rect = text.get_rect(center=start_button_rect.center)
    screen.blit(text, text_rect)

def option_button(screen):
    option_button_rect = pygame.Rect(740, 450, 200, 100)
    pygame.draw.rect(screen, (0, 0, 0), option_button_rect)
    font_size = 72
    font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render("Option", True, (255, 255, 255))
    text_rect = text.get_rect(center=option_button_rect.center)
    screen.blit(text, text_rect)

def quit_button(screen):
    quit_button_rect = pygame.Rect(740, 550, 200, 100)
    pygame.draw.rect(screen, (0, 0, 0), quit_button_rect)
    font_size = 72
    font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render("Quit", True, (255, 255, 255))
    text_rect = text.get_rect(center=quit_button_rect.center)
    screen.blit(text, text_rect)

def volume_option(screen):
    volume_option = pygame.Rect(700, 550, 200, 100)
    pygame.draw.rect(screen, (0, 0, 0), volume_option)
    font_size = 72
    font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render("Volume", True, (255, 255, 255))
    text_rect = text.get_rect(center=volume_option.center)
    screen.blit(text, text_rect)

def display_pillar(screen, pillar_x, pillar_height):
    pillar_image = pygame.image.load("graphics/enemy/pipe.png").convert_alpha()
    pillar_colour = (124, 252, 0) #green
    pillar_sec_colour = (124, 252, 0)
    pillar_width = 60 #width of pillar

    pillar_x_change = -4 #the changes in pillar

    pillar_x += pillar_x_change #the x of pillar will decrease thus will go left 
    if pillar_x <= -10: #if the x of pillar is at -10 it will reset again to 1600
        pillar_x = 1600
        pillar_height = random.randint(150, 450)
        
    screen.blit(pillar_image, (pillar_x, 0))
    screen.blit(pillar_image, (pillar_x, pillar_height + 300))

    bottom_pillar_height = 1000 - pillar_height - 430 # bottom pillar is 1000- (upper height) - 430(300 for gap and 130 from the ground) which is the ground which we wont be displaying the pillar )

    pygame.draw.rect(screen, pillar_colour, (pillar_x, 0, pillar_width, pillar_height)) #starts at x=1600 , y = 0 , width of the pillar, randint height of the pillar)
    pygame.draw.rect(screen, pillar_sec_colour, (pillar_x, pillar_height + 300, pillar_width, bottom_pillar_height)) #starts at x=1600 , randint height of the upper pillar and 300(gap) , width of the pillar, height of bottom pillar Line 55)


def collision_detection(player_x, player_y, pillar_x, pillar_height):
    player_rect = pygame.Rect(player_x, player_y, 50, 50) #player_rect will be from x and y of the player and the rect will be (85 by -50) -50 is because it will draw down the rectangle thus make it easier 
    pillar_rect1 = pygame.Rect(pillar_x, 0, 60, pillar_height)  #player_rect 1 will be from pillar x (upper) and the y =0 ; width of the pillar and the randint height of it
    pillar_rect2 = pygame.Rect(pillar_x, pillar_height + 200, 60, 1000 - pillar_height - 330) #player_rect 2 will be collision for the bottom_pillar calculation.. :P

    if player_rect.colliderect(pillar_rect1) or player_rect.colliderect(pillar_rect2):
        return True
    return False


def main(screen):
    clock = pygame.time.Clock()
    
    
    #player
    animation_controller = AnimationController()
    player_x, player_y = 400, 300  # Adjust the initial position as needed
    player_speed = 5 #speed of player moving
    gravity_speed = 1 # gravity speed


    #background
    background = pygame.image.load("graphics/background1.png").convert()
    background_width = background.get_width()
    background_rect = background.get_rect() #rect will be x and y of the background
    scroll = 0 #the starting background of the game when not scrolling is 0
    tiles = math.ceil(1600 / background_width) + 1 
    
    
    #multiple screens
    show_menu_screen = True
    show_game_screen = False
    show_option_screen = False
    selected_button = 0
    

    #blinking selected button
    selected_button_blink_timer = 0 
    selected_button_blink_cooldown = 350 
    is_button_visible = True


    #pillar varaibles...
    pillar_x_change = -4 #changes in x
    pillar_x = 1600 #x axis where the pillar starts at
    pillar_height = random.randint(150, 450) #random y 
    
    
    #duck egg varaibles...
    BLACK = (0, 0, 0)
    egg_sprite_sheet = spritesheet.SpriteSheet(pygame.image.load("graphics/white-duck/white-duck-walk.png").convert_alpha())#convert alpha makes transparency easier and make performance smoother
    egg_surface = egg_sprite_sheet.get_image(0, 40, 40, 1, BLACK)
    

    duck_egg_spawn_timer = pygame.USEREVENT + 1
    duck_egg_spawn_time = 5000 #sec for egg to spawn each time
    pygame.time.set_timer(duck_egg_spawn_timer, duck_egg_spawn_time) # generate an event signal for the event duck_egg_spawn_timer every 3 seconds. # bassically making my own event to make delays in the egg dropping :P
    spawned = True
    
    score = 0 

    
    
    while True:
        clock.tick(60)

        if show_menu_screen:
            screen.fill((0, 0, 0))
            start_button(screen)
            option_button(screen)
            quit_button(screen)
            selected_button_blink_timer += clock.get_time()

            #selection blinker
            if selected_button_blink_timer >= selected_button_blink_cooldown:
                selected_button_blink_timer = 0
                is_button_visible = not is_button_visible
            if is_button_visible:
                selection_button = pygame.Rect(540, 350 + selected_button * 100, 30, 100)
                pygame.draw.rect(screen, (255, 255, 255), selection_button)

        elif show_option_screen:
            screen.fill((0, 0, 0))  # Black screen for the option screen
            font_size = 72
            font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf", font_size)
            text = font_name.render("Controls", True, (255, 255, 255))
            text_rect = text.get_rect(center=(1600 // 2, 1000 // 2))
            screen.blit(text, text_rect)
            volume_option(screen)

            #blinking selection button
            selected_button_blink_timer += clock.get_time()
            if selected_button_blink_timer >= selected_button_blink_cooldown:
                selected_button_blink_timer = 0
                is_button_visible = not is_button_visible
            if is_button_visible:
                selection_button = pygame.Rect(420, 350 + selected_button * 100, 30, 100)
                pygame.draw.rect(screen, (255, 255, 255), selection_button)

            pygame.display.update()

        elif show_game_screen:
            screen.blit(background, (0, 0))

            #duck egg 
            for event in pygame.event.get():
                if spawned and event.type == duck_egg_spawn_timer:
                    egg_surface_rect = egg_surface.get_rect(center=(random.randint(100,800), random.randint(-100,-20)))
                    spawned = False
                if not spawned and egg_surface_rect != None and (pygame.Rect(player_x, player_y, 120, 120)).colliderect(egg_surface_rect):
                    score +=1
                    spawned = True
                    egg_surface_rect = None
                    print(score)
                    
                    
            #background scroll
            for i in range(0, tiles):
                screen.blit(background, (i * background_width + scroll, 0))
                background_rect.x = i * background_width + scroll

            scroll -= 2

            if abs(scroll) > background_width:
                scroll = 0


            #pillar 
            pillar_x += pillar_x_change
            if pillar_x <= -10:
                pillar_x = 1600
                pillar_height = random.randint(150, 450)
            display_pillar(screen, pillar_x, pillar_height)

            # Check for collision
            if collision_detection(player_x, player_y, pillar_x, pillar_height):
                show_game_screen = False  # Stop the game
                restart_game = True
                while restart_game == True:
                    for event in pygame.event.get(): 
                        if event.type == pygame.KEYDOWN :
                            if event.key == pygame.K_SPACE :#When space key is pressed, game restart
                                show_game_screen = True #Reset game
                                player_x, player_y = 400, 300
                                pillar_x = 1600
                                pillar_height = random.randint(150, 450)
                                scroll = 0
                                restart_game = False
                                score= 0
                            

            #keys WASD input
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                player_x -= player_speed
                animation_controller.action = 1  # Set the action for left movement #change action from 0 in animation to 1
            elif keys[pygame.K_d]:
                player_x += player_speed
                animation_controller.action = 1  # Set the action for right movement
            elif keys[pygame.K_w]:
                player_y -= player_speed + 5
                animation_controller.action = 1  # Set the action for up movement
            elif keys[pygame.K_s]:
                player_y += player_speed + 10
                animation_controller.action = 1  # Set the action for down movement
            else:
                player_y += player_speed
                animation_controller.frame = 0  # Reset frame when not moving
                
                

            # Freeze the player's movement on collision
            if not collision_detection(player_x, player_y, pillar_x, pillar_height):
                player_y += gravity_speed  # Apply gravity consistently

            # Ensure player stays within bounds
            player_y = max(0, min(player_y, 700))
            player_x = max(0, min(player_x, 800))

            animation_controller.update_animation(screen, player_x, player_y)

            
            if not spawned: #means that egg is already in the game 
                if egg_surface_rect.y < 850:
                    egg_surface_rect.y += 2
                    screen.blit(egg_surface, egg_surface_rect)
                elif egg_surface_rect.y == 850:
                    egg_surface_rect = None
                    spawned = True #means that the game need to spawn an egg
            
                

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if show_menu_screen:
                        if selected_button == 0:  # Start game
                            show_menu_screen = False
                            show_game_screen = True
                            animation_controller.setup_animation()
                        elif selected_button == 1:  # Option
                            show_menu_screen = False
                            show_option_screen = True
                        elif selected_button == 2:  # Quit
                            pygame.quit()
                            exit()
                        elif event.key == pygame.K_ESCAPE:
                            show_option_screen = False
                            show_menu_screen = True
                    elif show_option_screen:
                        if selected_button == 1:  # Controls
                            show_menu_screen = False
                            show_option_screen = False
                            screen.fill((0, 0, 0))
                            pygame.display.update()
                        elif selected_button == 2:  # Volume
                            pass
                elif event.key == pygame.K_DOWN:
                    if show_menu_screen:
                        if selected_button < 2:
                            selected_button += 1
                    if show_option_screen:
                        selected_button = 1
                        if selected_button <= 2:
                            selected_button += 1
                elif event.key == pygame.K_UP:
                    if show_menu_screen:
                        if selected_button > 0:
                            selected_button -= 1
                    if show_option_screen:
                        selected_button = 1
                        if selected_button > 1:
                            selected_button -= 1
                elif event.key == pygame.K_ESCAPE:
                    show_menu_screen = True
                    show_game_screen = False
                    show_option_screen = False


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Duck On The Run!")
    WIDTH, HEIGHT = (1600, 1000)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    main(screen)
