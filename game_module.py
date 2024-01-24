import pygame
from animation import AnimationController
import math
import random


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
    pillar_colour = (124, 252, 0)
    pillar_sec_colour = (124, 252, 0)
    pillar_width = 60
    
    pillar_x_change = -4

    pillar_x += pillar_x_change
    if pillar_x <= -10:
        pillar_x = 1600
        pillar_height = random.randint(150, 450)
        
    bottom_pillar_height = 1000 - pillar_height - 430
        
    pygame.draw.rect(screen, pillar_colour, (pillar_x, 0, pillar_width, pillar_height))
    pygame.draw.rect(screen, pillar_sec_colour, (pillar_x, pillar_height + 300, pillar_width, bottom_pillar_height))


def collision_detection(player_x, player_y, pillar_x, pillar_height):
    player_rect = pygame.Rect(player_x, player_y, 85, 85)
    pillar_rect1 = pygame.Rect(pillar_x, 0, 60, pillar_height)
    pillar_rect2 = pygame.Rect(pillar_x, pillar_height + 200, 60, 1000 - pillar_height - 330)

    if player_rect.colliderect(pillar_rect1) or player_rect.colliderect(pillar_rect2):
        return True
    return False

def main(screen):
    clock = pygame.time.Clock()
    animation_controller = AnimationController()
    player_x, player_y = 400, 300  # Adjust the initial position as needed
    player_speed = 5
    gravity_speed = 1
    
    background = pygame.image.load("graphics/background1.png").convert()
    background_width = background.get_width()
    background_rect = background.get_rect()
    scroll = 0
    tiles = math.ceil(1600 / background_width ) + 1

    show_menu_screen = True
    show_game_screen = False
    show_option_screen = False
    selected_button = 0

    selected_button_blink_timer = 0
    selected_button_blink_cooldown = 350
    is_button_visible = True

    pillar_x_change = -4
    pillar_x = 1600
    pillar_height = random.randint(150, 450)

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
                
        elif show_option_screen :
            screen.fill((0, 0, 0))  # Black screen for the option screen
            font_size = 72
            font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf", font_size)
            text = font_name.render("Controls", True, (255, 255, 255))
            text_rect = text.get_rect(center=(1600 // 2, 1000 // 2))
            screen.blit(text, text_rect)
            volume_option(screen)
            
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
            
            for i in range(0,tiles) :
                screen.blit(background, (i * background_width + scroll, 0))
                background_rect.x = i * background_width + scroll
                
            scroll -= 2
            
            if abs(scroll) > background_width :
                scroll = 0

            pillar_x += pillar_x_change
            if pillar_x <= -10:
                pillar_x = 1600
                pillar_height = random.randint(150, 450)
            display_pillar(screen, pillar_x, pillar_height)

            # Check for collision
            if collision_detection(player_x, player_y, pillar_x, pillar_height):
                screen.fill('Yellow') #Display score
                show_game_screen = False #Stop game
                pygame.display.update()

                restart_game = False
                while not restart_game:
                    for event in pygame.event.get(): 
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #When space key is pressed, game restart
                            restart_game = True
                            show_game_screen = True #Reset game
                            player_x, player_y = 400, 300
                            pillar_x = 1600
                            pillar_height = random.randint(150, 450)
                            scroll = 0
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            restart_game = True  # Go back to the menu
                            show_menu_screen = True
                            show_game_screen = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                player_x -= player_speed
                animation_controller.action = 1  # Set the action for left movement
            elif keys[pygame.K_d]:
                player_x += player_speed
                animation_controller.action = 0  # Set the action for right movement
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
            pygame.display.update()
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
                    if show_menu_screen :
                        if selected_button < 2:
                            selected_button += 1
                    if show_option_screen :
                        selected_button = 1
                        if selected_button <= 2:
                            selected_button += 1
                elif event.key == pygame.K_UP:
                    if show_menu_screen :
                        if selected_button > 0:
                            selected_button -= 1
                    if show_option_screen :
                        selected_button = 1
                        if selected_button > 1:
                            selected_button -= 1
                    
                elif event.key == pygame.K_ESCAPE:
                    show_menu_screen = True
                    show_game_screen = False
                    show_option_screen = False
                
                

        pygame.display.update()

if __name__ == "_main_":
    pygame.init()
    pygame.display.set_caption("Duck On The Run!")
    WIDTH, HEIGHT = (1600, 1000)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    main(screen)