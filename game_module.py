import pygame
from animation import AnimationController
import math
import random
import spritesheet
from pygame import mixer
#remember to add Duck in Danger/ to each path when submitting as a ZIP file

#MeiTing Part
pygame.mixer.init() #Initialize mixer
pygame.mixer.music.load("background.mp3") # Load music file
pygame.mixer.music.set_volume(0.5)  # Set volume (optional), Adjust the volume as needed
pygame.mixer.music.play(-1)  # Play musicThe -1 argument makes the music loop indefinitely

game_over = pygame.mixer.Sound('game_over.mp3')
game_over.set_volume(1.0)

def intro_screen(screen):
    intro = pygame.image.load("graphics/intro.png").convert()
    intro = pygame.transform.scale(intro, (1550, 950))
    screen.blit(intro, (25, 25))
    pygame.display.update()

    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting_for_key = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()

#Danny Part
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
    
def controls_option(screen) :
    controls_option = pygame.Rect(700, 550, 200, 100)
    pygame.draw.rect(screen, (0, 0, 0), controls_option)
    screen.fill((0, 0, 0))  # Black screen for the option screen
    font_size = 72
    font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render("Controls", True, (255, 255, 255))
    text_rect = text.get_rect(center=(800,500))
    screen.blit(text, text_rect)
    
def volume_off_option(screen):
    volume_off_option = pygame.Rect(700, 550, 200, 100)
    pygame.draw.rect(screen, (0, 0, 0), volume_off_option)
    font_size = 72
    font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render("Off", True, (255, 255, 255))
    text_rect = text.get_rect(center=volume_off_option.center)
    screen.blit(text, text_rect)
    
def volume_on_option(screen) :
    volume_on_option = pygame.Rect(700, 200, 200, 100)
    pygame.draw.rect(screen, (0, 0, 0), volume_on_option)
    font_size = 72
    font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render("On", True, (255, 255, 255))
    text_rect = text.get_rect(center=(800,500))
    screen.blit(text, text_rect)

def how_to_scroll_up_down(screen) :
    how_to_scroll_up_down = pygame.Rect(200, 200, 200, 100)
    pygame.draw.rect(screen, (0, 0, 0), how_to_scroll_up_down)
    font_size = 20
    font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render("\"Up\" and \"Down\" Key to scroll ", True, (255, 255, 255))
    text_rect = text.get_rect(center=(270,900))
    screen.blit(text, text_rect)
    
def how_to_scroll_enter(screen) :
    how_to_scroll_enter = pygame.Rect(200, 200, 200, 100)
    pygame.draw.rect(screen, (0, 0, 0), how_to_scroll_enter)
    font_size = 20
    font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render("\"Enter\" Key to select", True, (255, 255, 255))
    text_rect = text.get_rect(center=(200,950))
    screen.blit(text, text_rect)
    
def controls_controls_option(screen) :
    font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf", 30)
    up_text = font_name.render("\"Up\" Key to scroll", True, (255, 255, 255))
    down_text = font_name.render("\"Down\" Key to scroll", True, (255, 255, 255))
    select_text = font_name.render("\"Enter\" Key to select", True, (255, 255, 255))
    esc_text = font_name.render("\"Esc\" Key to open menu", True, (255, 255, 255))
    menu_text = pygame.font.Font("fonts/8-BIT WONDER.ttf", 50).render("Menu", True, (255, 255, 255))
    w_text = font_name.render("\"W\" Key to move up", True, (255, 255, 255))
    a_text = font_name.render("\"A\" Key to move left", True, (255, 255, 255))
    s_text = font_name.render("\"S\" Key to move down", True, (255, 255, 255))
    d_text = font_name.render("\"D\" Key to move right", True, (255, 255, 255))
    restart_text = font_name.render("\"Enter\" Key to restart", True, (255, 255, 255))
    in_game_text = pygame.font.Font("fonts/8-BIT WONDER.ttf", 50).render("In Game", True, (255, 255, 255))
    screen.blit(up_text, up_text.get_rect(center=(800,200)))
    screen.blit(down_text, down_text.get_rect(center=(800,250)))
    screen.blit(select_text, select_text.get_rect(center=(800,300)))
    screen.blit(esc_text, esc_text.get_rect(center=(800,750)))
    screen.blit(menu_text, menu_text.get_rect(center=(800,140)))
    screen.blit(w_text, w_text.get_rect(center=(800,500)))
    screen.blit(a_text, a_text.get_rect(center=(800,550)))
    screen.blit(s_text, s_text.get_rect(center=(800,600)))
    screen.blit(d_text, d_text.get_rect(center=(800,650)))
    screen.blit(restart_text, restart_text.get_rect(center=(800,700)))
    screen.blit(in_game_text, in_game_text.get_rect(center=(800,440)))
    
    

    

#MeiTing Part
def display_pillar(screen, pillar_x, pillar_height):
    upper_pipe_image = pygame.image.load("graphics/enemy/upper_pillar.png").convert_alpha()
    lower_pipe_image = pygame.image.load("graphics/enemy/lower_pillar.png").convert_alpha()
    pillar_colour = (124, 252, 0)  # green
    pillar_sec_colour = (124, 252, 0)
    pillar_width = 60  # width of pillar

    pillar_x_change = -4  # the changes in pillar

    pillar_x += pillar_x_change  # the x of pillar will decrease thus will go left
    if pillar_x <= -10:  # if the x of pillar is at -10 it will reset again to 1600
        pillar_x = 1600
        pillar_height = random.randint(150, 450)

    bottom_pillar_height = 1000 - pillar_height - 430  # bottom pillar is 1000- (upper height) - 430(300 for gap and 130 from the ground) which is the ground which we won't be displaying the pillar

    # Draw the rectangles
    pygame.draw.rect(screen, pillar_colour, (pillar_x, 0, pillar_width, pillar_height))  # upper pillar
    pygame.draw.rect(screen, pillar_sec_colour,(pillar_x, pillar_height + 300, pillar_width, bottom_pillar_height))  # bottom pillar

    upper_pipe_image = pygame.transform.scale(upper_pipe_image, (pillar_width + 5, pillar_height)) # scale the image to the rect of pillar
    lower_pipe_image = pygame.transform.scale(lower_pipe_image, (pillar_width + 5, bottom_pillar_height))
    
    screen.blit(upper_pipe_image, (pillar_x-3, 0)) #blit image onto the pillar and -3 to move it to the left a bit
    screen.blit(lower_pipe_image, (pillar_x-3, pillar_height + 300))


def collision_detection(player_x, player_y, pillar_x, pillar_height):
    player_rect = pygame.Rect(player_x, player_y, 40, 40) #player_rect will be from x and y of the player 
    pillar_rect1 = pygame.Rect(pillar_x, 0, 60, pillar_height)  #player_rect 1 will be from pillar x (upper) and the y =0 ; width of the pillar and the randint height of it
    pillar_rect2 = pygame.Rect(pillar_x, pillar_height + 200, 60, 1000 - pillar_height - 330) #player_rect 2 will be collision for the bottom_pillar calculation.. :P

    if player_rect.colliderect(pillar_rect1) or player_rect.colliderect(pillar_rect2):
        return True
    return False

#Danny Part
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
    tiles = math.ceil(1600 / background_width) + 1 # basically 2 images next to each other
    
    
    #multiple screens
    show_intro_screen = True
    show_menu_screen = True
    show_game_screen = False
    show_option_screen = False
    show_volume_screen = False
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
    egg_sprite_sheet = spritesheet.SpriteSheet(pygame.image.load("graphics/duck egg/duckegg.png").convert_alpha())#convert alpha makes transparency easier and make performance smoother
    egg_surface = egg_sprite_sheet.get_image(0, 40, 40, 1, BLACK)
    

    duck_egg_spawn_timer = pygame.USEREVENT + 10
    duck_egg_spawn_time = 1000 #sec for egg to spawn each time
    pygame.time.set_timer(duck_egg_spawn_timer, duck_egg_spawn_time) # generate an event signal for the event duck_egg_spawn_timer every 3 seconds. # bassically making my own event to make delays in the egg dropping :P
    spawned = True
    
    score = 0 

    
    
    while True:
        clock.tick(60)
        if show_intro_screen:
            intro_screen(screen)
            show_intro_screen = False
            show_menu_screen = True

        if show_menu_screen:
            screen.fill((0, 0, 0))
            start_button(screen)
            option_button(screen)
            quit_button(screen)
            how_to_scroll_up_down(screen)
            how_to_scroll_enter(screen)
            selected_button_blink_timer += clock.get_time()

            #selection blinker
            if selected_button_blink_timer >= selected_button_blink_cooldown:
                selected_button_blink_timer = 0
                is_button_visible = not is_button_visible
            if is_button_visible:
                selection_button = pygame.Rect(540, 350 + selected_button * 100, 30, 100)
                pygame.draw.rect(screen, (255, 255, 255), selection_button)

        elif show_option_screen:
            screen.fill((0, 0, 0))
            controls_option(screen)
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
            
        elif show_volume_screen :
            screen.fill((0, 0, 0))
            volume_off_option(screen)
            volume_on_option(screen)
            
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
                    egg_surface_rect = egg_surface.get_rect(center=(random.randint(100,800), random.randint(-100,-20))) #rect of the egg at random x and y
                    spawned = False #becomes False after spawning or hitting the ground
                if not spawned and egg_surface_rect != None and (pygame.Rect(player_x, player_y, 120, 120)).colliderect(egg_surface_rect):
                    score +=1 #+1 when collide with egg
                    spawned = True #spawns the egg when True
                    egg_surface_rect = None #return the rect to none and it will then generate a new rect 
                    
                    
            #background scroll
            for i in range(0, tiles):
                screen.blit(background, (i * background_width + scroll, 0))
                
            scroll -= 2 #after drawing all the tiles in the loop; sroll will be -2 ; to make it scroll

            if abs(scroll) > background_width: #meaning the background had went past 2 ;it reset the scroll to 0
                scroll = 0


#MeiTing Part

            #pillar 
            pillar_x += pillar_x_change
            if pillar_x <= -10:
                pillar_x = 1600
                pillar_height = random.randint(150, 450)
            display_pillar(screen, pillar_x, pillar_height)

            # Check for collision
            if collision_detection(player_x, player_y, pillar_x, pillar_height):
                game_over.play()
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

#YongXin Part
                text_score = open("demofile2.txt", "a")
                text_score.write(f"{score}\n")
                new_score = score
                print(new_score)
                text_score.close()
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
                            




#DANNY Part
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
                
#MeiTing Part
            # Freeze the player's movement on collision
            if not collision_detection(player_x, player_y, pillar_x, pillar_height):
                player_y += gravity_speed  # Apply gravity consistently


#DANNY Part
            # Ensure player stays within bounds
            player_y = max(0, min(player_y, 700))
            player_x = max(0, min(player_x, 800))

            animation_controller.update_animation(screen, player_x, player_y) #updates animation on screen at the player coords

            
            if not spawned: #means that egg is already in the game 
                if egg_surface_rect.y < 850:
                    egg_surface_rect.y += 2
                    screen.blit(egg_surface, egg_surface_rect)
                elif egg_surface_rect.y == 850: #when egg hits the ground
                    egg_surface_rect = None
                    spawned = True #means that the game need to spawn an egg
            
                

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:# press enter key
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
                            controls_controls_option(screen)
                            pygame.display.update()
                        elif selected_button == 2:  # Volume
                            show_menu_screen = False
                            show_option_screen = False
                            show_volume_screen = True
                    elif show_volume_screen:
                        if selected_button == 1:  # Controls
                            pygame.mixer.music.play()
                        elif selected_button == 2:  # Volume
                            pygame.mixer.music.stop()
                           
                            
                           
                            
                elif event.key == pygame.K_DOWN: #basic scrollig through the menu
                    if show_menu_screen:
                        if selected_button < 2:
                            selected_button += 1
                    if show_option_screen:
                        selected_button = 1
                        if selected_button <= 2:
                            selected_button += 1
                    if show_volume_screen:
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
                    if show_volume_screen:
                        selected_button = 1
                        if selected_button > 1:
                            selected_button -= 1
                elif event.key == pygame.K_ESCAPE:
                    show_menu_screen = True
                    show_game_screen = False
                    show_option_screen = False
                    show_volume_screen = False


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Duck In Danger!")
    WIDTH, HEIGHT = (1600, 1000)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    main(screen)
