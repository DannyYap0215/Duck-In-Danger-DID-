import pygame
from animation import AnimationController
import math
import random
import spritesheet
from pygame import mixer
# Remember to add Duck in Danger to each path when submitting as a ZIP file

# MeiTing Part
pygame.mixer.init () # Initialize mixer
pygame.mixer.music.load("audio/background.mp3") # Load music file
pygame.mixer.music.set_volume(0.5)  # Set volume
pygame.mixer.music.play(-1)  # The -1 argument makes the music loop indefinitely

# YongXin Part
# Load sound effects
score_sound = pygame.mixer.Sound("audio/score.mp3")
score_sound.set_volume(1.0)

game_over_sound = pygame.mixer.Sound("audio/game_over.mp3")
game_over_sound.set_volume(1.0)

# MeiTing Part
def intro_screen(screen) :
    intro = pygame.image.load ("graphics/intro.png") .convert () #Load image
    intro = pygame.transform.scale (intro, (1550, 950) ) #Resize the image
    screen.blit (intro, (25, 25) ) #Display in specified position
    pygame.display.update () #Update the display to show the intro

    waiting_for_key = True
    while waiting_for_key :
        for event in pygame.event.get () :
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE : #Checked if the space key is preesed to exit the loop
                waiting_for_key = False
            elif event.type == pygame.QUIT : #Checked if the window closed to exit the program
                pygame.quit ()
                exit ()

# Danny Part
def start_button(screen) :
    start_button_rect = pygame.Rect (740, 350, 200, 100)
    pygame.draw.rect (screen, (0, 0, 0) , start_button_rect)
    font_size = 72
    font_name = pygame.font.Font ("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render ("Start", True, (255, 255, 255) )
    text_rect = text.get_rect (center = start_button_rect.center)
    screen.blit (text, text_rect)

def option_button(screen) :
    option_button_rect = pygame.Rect (740, 450, 200, 100)
    pygame.draw.rect (screen, (0, 0, 0) , option_button_rect)
    font_size = 72
    font_name = pygame.font.Font ("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render ("Option", True, (255, 255, 255) )
    text_rect = text.get_rect (center = option_button_rect.center)
    screen.blit (text, text_rect)

def quit_button(screen) :
    quit_button_rect = pygame.Rect (740, 550, 200, 100)
    pygame.draw.rect (screen, (0, 0, 0) , quit_button_rect)
    font_size = 72
    font_name = pygame.font.Font ("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render ("Quit", True, (255, 255, 255) )
    text_rect = text.get_rect (center = quit_button_rect.center)
    screen.blit (text, text_rect)

def volume_option(screen) :
    volume_option = pygame.Rect (700, 550, 200, 100)
    pygame.draw.rect (screen, (0, 0, 0) , volume_option)
    font_size = 72
    font_name = pygame.font.Font ("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render ("Volume", True, (255, 255, 255) )
    text_rect = text.get_rect (center = volume_option.center)
    screen.blit (text, text_rect)

def controls_option(screen) :
    controls_option = pygame.Rect (700, 550, 200, 100)
    pygame.draw.rect (screen, (0, 0, 0) , controls_option)
    screen.fill ( (0, 0, 0) )  # Black screen for the option screen
    font_size = 72
    font_name = pygame.font.Font ("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render ("Controls", True, (255, 255, 255) )
    text_rect = text.get_rect (center = (800,500) )
    screen.blit (text, text_rect)
    
def volume_off_option(screen) :
    volume_off_option = pygame.Rect (700, 550, 200, 100)
    pygame.draw.rect (screen, (0, 0, 0) , volume_off_option)
    font_size = 72
    font_name = pygame.font.Font ("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render ("Off", True, (255, 255, 255) )
    text_rect = text.get_rect (center = volume_off_option.center)
    screen.blit (text, text_rect)
    
def volume_on_option(screen) :
    volume_on_option = pygame.Rect (700, 200, 200, 100)
    pygame.draw.rect (screen, (0, 0, 0) , volume_on_option)
    font_size = 72
    font_name = pygame.font.Font ("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render ("On", True, (255, 255, 255) )
    text_rect = text.get_rect (center = (800,500) )
    screen.blit (text, text_rect)

def how_to_scroll_up_down(screen) :
    how_to_scroll_up_down = pygame.Rect (200, 200, 200, 100)
    pygame.draw.rect (screen, (0, 0, 0) , how_to_scroll_up_down)
    font_size = 20
    font_name = pygame.font.Font ("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render ("[ Up ] and [ Down ] Key to scroll ", True, (255, 255, 255) )
    text_rect = text.get_rect (center = (310,890) ) 
    screen.blit (text, text_rect)
    
def how_to_scroll_enter(screen) :
    how_to_scroll_enter = pygame.Rect (200, 200, 200, 100)
    pygame.draw.rect (screen, (0, 0, 0) , how_to_scroll_enter)
    font_size = 20
    font_name = pygame.font.Font ("fonts/8-BIT WONDER.ttf", font_size)
    text = font_name.render ("[ Enter ] Key to select", True, (255, 255, 255) )
    text_rect = text.get_rect ( center = (230,920) ) 
    screen.blit (text, text_rect)

# MeiTing Part
def controls_controls_option(screen) :
    font_name = pygame.font.Font ("fonts/8-BIT WONDER.ttf", 30)

    menu_text = pygame.font.Font ("fonts/8-BIT WONDER.ttf", 50) .render ("Menu", True, (255, 255, 255) )
    up_text = font_name.render ("[ Up ]  Key to scroll", True, (255, 255, 255) )
    down_text = font_name.render ("[ Down ]  Key to scroll", True, (255, 255, 255) )
    select_text = font_name.render ("[ Enter ]  Key to select", True, (255, 255, 255) )

    in_game_text = pygame.font.Font ("fonts/8-BIT WONDER.ttf", 50) .render ("In Game", True, (255, 255, 255) )
    w_text = font_name.render ("[ W ]  Key to move up", True, (255, 255, 255) )
    a_text = font_name.render ("[ A ]  Key to move left", True, (255, 255, 255) )
    s_text = font_name.render ("[ S ]  Key to move down", True, (255, 255, 255) )
    d_text = font_name.render ("[ D ]  Key to move right", True, (255, 255, 255) )
    restart_text = font_name.render ("[ Space ]  Key to restart", True, (255, 255, 255) )
    esc_text = font_name.render ("[ Esc ]  Key to open menu", True, (255, 255, 255) )

    screen.blit (menu_text, menu_text.get_rect (center = (800, 200) ) ) 
    screen.blit (up_text, up_text.get_rect (center = (800, 260) ) ) 
    screen.blit (down_text, down_text.get_rect (center = (800, 310) ) ) 
    screen.blit (select_text, select_text.get_rect (center = (800, 360) ) ) 

    screen.blit (in_game_text, in_game_text.get_rect (center = (800, 500) ) ) 
    screen.blit (w_text, w_text.get_rect (center = (800, 550) ) ) 
    screen.blit (a_text, a_text.get_rect (center = (800, 600) ) ) 
    screen.blit (s_text, s_text.get_rect (center = (800, 650) ) ) 
    screen.blit (d_text, d_text.get_rect (center = (800, 700) ) ) 
    screen.blit (restart_text, restart_text.get_rect (center = (800, 750) ) ) 
    screen.blit (esc_text, esc_text.get_rect (center = (800, 800) ) ) 

def display_pillar(screen, pillar_x, pillar_height) :
    upper_pipe_image = pygame.image.load ("graphics/enemy/upper_pillar.png") .convert_alpha ()
    lower_pipe_image = pygame.image.load ("graphics/enemy/lower_pillar.png") .convert_alpha ()
    pillar_colour = (124, 252, 0)  # Green
    pillar_sec_colour = (124, 252, 0)
    pillar_width = 60  # Width of pillar
    
    pillar_x_change = -4  # The changes in pillar

    pillar_x += pillar_x_change  # The x of pillar will decrease thus will go left
    if pillar_x <= -10 :  # If the x of pillar is at -10 it will reset again to 1600
        pillar_x = 1600
        pillar_height = random.randint (150, 450)

    bottom_pillar_height = 1000 - pillar_height - 430  # Bottom pillar is 1000- (upper height) - 430(300 for gap and 130 from the ground) which is the ground which we won't be displaying the pillar

    # Draw the rectangles
    pygame.draw.rect (screen, pillar_colour, (pillar_x, 0, pillar_width, pillar_height) )  # Upper pillar
    pygame.draw.rect (screen, pillar_sec_colour, (pillar_x, pillar_height + 300, pillar_width, bottom_pillar_height) )  # Bottom pillar

    upper_pipe_image = pygame.transform.scale (upper_pipe_image, (pillar_width + 5, pillar_height) ) # Scale the image to the rect of pillar
    lower_pipe_image = pygame.transform.scale (lower_pipe_image, (pillar_width + 5, bottom_pillar_height) )
    
    screen.blit (upper_pipe_image, (pillar_x-3, 0) ) # Blit image onto the pillar and -3 to move it to the left a bit
    screen.blit (lower_pipe_image, (pillar_x-3, pillar_height + 300) )

def collision_detection(player_x, player_y, pillar_x, pillar_height) :
    player_rect = pygame.Rect(player_x, player_y, 40, 40) # Player_rect will be from x and y of the player 
    pillar_rect1 = pygame.Rect(pillar_x, 0, 60, pillar_height)  # Player_rect 1 will be from pillar x (upper) and the y =0 ; width of the pillar and the randint height of it
    pillar_rect2 = pygame.Rect(pillar_x, pillar_height + 200, 60, 1000 - pillar_height - 330) # Player_rect 2 will be collision for the bottom_pillar calculation.. :P

    if player_rect.colliderect(pillar_rect1) or player_rect.colliderect(pillar_rect2) :
        return True
    return False

# Danny Part
def main(screen) :
    clock = pygame.time.Clock()
    
    # Player
    animation_controller = AnimationController()
    player_x, player_y = 400, 300  # Adjust the initial position as needed
    player_speed = 5 # Speed of player moving
    gravity_speed = 1 # Gravity speed

    # Background
    background = pygame.image.load ("graphics/background1.png").convert()
    background_width = background.get_width()
    background_rect = background.get_rect() # Rect will be x and y of the background
    scroll = 0 # The starting background of the game when not scrolling is 0
    tiles = math.ceil(1600 / background_width) + 1 # Basically 2 images next to each other
    
    # Multiple screens
    show_intro_screen = True
    show_menu_screen = True
    show_game_screen = False
    show_option_screen = False
    show_controls_screen = False
    show_volume_screen = False
    selected_button = 0
    
    # Blinking selected button    
    selected_button_blink_timer = 0
    selected_button_blink_cooldown = 350
    is_button_visible = True

    # Pillar varaibles...
    pillar_x_change = -4 # Changes in x
    pillar_x = 1600 # X axis where the pillar starts at
    pillar_height = random.randint(150, 450) # Random y 

    # Duck egg varaibles...
    BLACK = (0, 0, 0)
    egg_sprite_sheet = spritesheet.SpriteSheet(pygame.image.load ("graphics/duck egg/duckegg.png") .convert_alpha () ) # Convert alpha makes transparency easier and make performance smoother
    egg_surface = egg_sprite_sheet.get_image(0, 40, 40, 1, BLACK)
    
    duck_egg_spawn_timer = pygame.USEREVENT + 10
    duck_egg_spawn_time = 1000 # Sec for egg to spawn each time
    pygame.time.set_timer(duck_egg_spawn_timer, duck_egg_spawn_time) # Generate an event signal for the event duck_egg_spawn_timer every 3 seconds. # bassically making my own event to make delays in the egg dropping :P
    spawned = True

    # YongXin Part
    score = 0
    pass_pillar = False
    pass_current_pillar = False  # New variable to track passing the current pillar

    # Score screen
    font = pygame.font.Font("fonts/8-BIT WONDER.ttf", 72)
    game_name = "Duck In Danger"
    game_name_text = font.render(game_name, True, (255, 255, 255) )
    game_name_rect = game_name_text.get_rect(center = (800, 150) )

    duck_stand = pygame.image.load("graphics/white-duck/white-duck-stand.png") .convert_alpha ()
    duck_stand = pygame.transform.rotozoom(duck_stand, 0, 0.65)
    duck_stand_rect = duck_stand.get_rect(center = (800,400) )

    font = pygame.font.Font("fonts/8-BIT WONDER.ttf", 30)
    restart = "Press space to restart"
    restart_text = font.render(restart, True, (255, 255, 255) )
    restart_rect = restart_text.get_rect(center = (800, 900) )
    
    while True :
        clock.tick(60)

        # MeiTing Part
        if show_intro_screen :
            intro_screen(screen)
            show_intro_screen = False
            show_menu_screen = True

        # Danny Part
        if show_menu_screen :
            screen.fill( (0, 0, 0) )
            start_button(screen)
            option_button(screen)
            quit_button(screen)
            how_to_scroll_up_down(screen)
            how_to_scroll_enter(screen)
            selected_button_blink_timer += clock.get_time()

            # Selection blinker
            if selected_button_blink_timer >= selected_button_blink_cooldown :
                selected_button_blink_timer = 0
                is_button_visible = not is_button_visible
            if is_button_visible :
                selection_button = pygame.Rect(540, 350 + selected_button * 100, 30, 100)
                pygame.draw.rect(screen, (255, 255, 255) , selection_button)

        elif show_option_screen :
            screen.fill( (0, 0, 0) )  # Black screen for the option screen
            controls_option(screen)
            volume_option(screen)
            
            # Blinking selection button
            selected_button_blink_timer += clock.get_time ()
            if selected_button_blink_timer >= selected_button_blink_cooldown :
                selected_button_blink_timer = 0
                is_button_visible = not is_button_visible
            if is_button_visible :
                selection_button = pygame.Rect (420, 350 + selected_button * 100, 30, 100)
                pygame.draw.rect (screen, (255, 255, 255) , selection_button)
            
            pygame.display.update()
        # YongXin Part
        elif show_controls_screen :
            screen.fill ( (0, 0, 0) )
            controls_controls_option(screen)
            pygame.display.update()
        # Danny Part
        elif show_volume_screen :
            screen.fill( (0, 0, 0) )
            volume_off_option(screen)
            volume_on_option(screen)
            
            # Blinking selection button
            selected_button_blink_timer += clock.get_time ()
            if selected_button_blink_timer >= selected_button_blink_cooldown :
                selected_button_blink_timer = 0
                is_button_visible = not is_button_visible
            if is_button_visible :
                selection_button = pygame.Rect (420, 350 + selected_button * 100, 30, 100)
                pygame.draw.rect (screen, (255, 255, 255) , selection_button)

            pygame.display.update ()
            
        elif show_game_screen :
            screen.blit(background, (0, 0) )
            
            # Duck egg 
            for event in pygame.event.get () :
                if spawned and event.type == duck_egg_spawn_timer : 
                    egg_surface_rect = egg_surface.get_rect (center = (random.randint (100,800) , random.randint (-100,-20) ) ) # Rect of the egg at random x and y
                    spawned = False # Becomes False after spawning or hitting the ground
                if not spawned and egg_surface_rect != None and (pygame.Rect (player_x, player_y, 120, 120) ).colliderect (egg_surface_rect) :
                    score +=1 # +1 when collide with egg
                    spawned = True # Spawns the egg when True
                    egg_surface_rect = None # Return the rect to none and it will then generate a new rect 
                    score_sound.play()
                    
            # Background scroll
            for i in range(0, tiles) :
                screen.blit(background, (i * background_width + scroll, 0) )
                
            scroll -= 2 # After drawing all the tiles in the loop; sroll will be -2 ; to make it scroll

            if abs(scroll) > background_width: # Meaning the background had went past 2 ;it reset the scroll to 0
                scroll = 0
            
# MeiTing Part
            # Pillar             
            pillar_x += pillar_x_change
            if pillar_x <= -10 :
                pillar_x = 1600
                pillar_height = random.randint(150, 450)
                pass_current_pillar = False  # Reset pass_current_pillar for the new pillar (YongXin Part)
            display_pillar(screen, pillar_x, pillar_height)
  
# YongXin Part          
            # Check for collision
            if collision_detection(player_x, player_y, pillar_x, pillar_height) :
                game_over_sound.play()
                show_game_screen = False # Stop game
                screen.fill( (131,192,223) )
                screen.blit(game_name_text, game_name_rect)
                screen.blit(duck_stand, duck_stand_rect)
            
                font = pygame.font.Font ("fonts/8-BIT WONDER.ttf", 72)
                score_num = str(score) 
                score_display = "Score " + str(score)                    
                score_text = font.render (score_display, True, (255, 255, 255) )
                score_rect = score_text.get_rect (center = (800, 650) )
                screen.blit(score_text, score_rect) # Display score
                text_score = open ("score.txt", "a") # Store score and find high score
                text_score.write (f"{score_num}\n")
                text_score.close()
                with open("score.txt", "r") as file:
                    numbers = [int(line.strip()) for line in file.readlines()]
                    highest = max(numbers)
                    highest = str(highest)
                
                
                highest_score_display = "High Score " + highest                  
                highest_score_text = font.render (highest_score_display, True, (255, 255, 255) )
                highest_score_rect = highest_score_text.get_rect(center = (800, 800) )

                screen.blit(highest_score_text, highest_score_rect) # Display high score
                screen.blit(restart_text, restart_rect) # Instruction to restart game
                pass_current_pillar = False

                pygame.display.update()

                restart_game = False
                while not restart_game :
                    for event in pygame.event.get() : 
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # When space key is pressed, game restart
                            restart_game = True
                            show_game_screen = True # Reset game
                            score = 0 # Reset score
                            player_x, player_y = 400, 300
                            pillar_x = 1600
                            pillar_height = random.randint (150, 450)
                            egg_surface_rect = None
                            spawned = True # Means that the game need to spawn an egg
                            scroll = 0
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :  
                            show_menu_screen = True                                  
                            restart_game = True  # Go back to the menu
                            show_game_screen = True # Reset game
                            score = 0 # Reset score
                            player_x, player_y = 400, 300
                            pillar_x = 1600
                            pillar_height = random.randint (150, 450)
                            egg_surface_rect = None
                            spawned = True # Means that the game need to spawn an egg
                            scroll = 0

            # Check for the passage of a pillar and increment the score
            if not pass_current_pillar and player_x > pillar_x + 60 :
                score += 1
                pass_current_pillar = True
                # Play the score sound
                score_sound.play()

            # Reset to ensure the game can detect the player passes a pillar next time
            if pillar_x <= -10:
                pass_pillar = False
                pass_current_pillar = False

# Danny Part
            # Keys WASD input
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] :
                player_x -= player_speed
                animation_controller.action = 1  # Set the action for left movement
            elif keys[pygame.K_d] :
                player_x += player_speed
                animation_controller.action = 1  # Set the action for right movement
            elif keys[pygame.K_w] :
                player_y -= player_speed + 5
                animation_controller.action = 1  # Set the action for up movement
            elif keys[pygame.K_s] :
                player_y += player_speed + 10
                animation_controller.action = 1  # Set the action for down movement
            else :
                player_y += player_speed
                animation_controller.frame = 0  # Reset frame when not moving
                
# MeiTing Part
             # Freeze the player's movement on collision
            if not collision_detection (player_x, player_y, pillar_x, pillar_height) :    
                player_y += gravity_speed  # Apply gravity consistently

# Danny Part
            # Ensure player stays within bounds
            player_y = max(0, min (player_y, 700) )
            player_x = max(0, min (player_x, 800) )
                
            animation_controller.update_animation(screen, player_x, player_y)

            if not spawned : # Means that egg is already in the game 
                if egg_surface_rect.y < 850 :
                    egg_surface_rect.y += 2
                    screen.blit (egg_surface, egg_surface_rect)
                elif egg_surface_rect.y == 850 : # When egg hits the ground
                    egg_surface_rect = None
                    spawned = True # Means that the game need to spawn an egg
            
 # YongXin Part            
            # Display the score during the game
            font = pygame.font.Font("fonts/8-BIT WONDER.ttf", 45)
            score_text = "Score " + str(score)
            text = font.render(score_text, True, (255, 255, 255) )
            text_rect = text.get_rect(center = (1400, 50) )
            screen.blit(text, text_rect)

            pygame.display.update()

        pygame.display.update()  

# Danny Part
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RETURN :
                    if show_menu_screen :
                        if selected_button == 0 :  # Start game
                            show_menu_screen = False
                            show_game_screen = True
                            animation_controller.setup_animation()
                        elif selected_button == 1 :  # Option
                            show_menu_screen = False
                            show_option_screen = True
                        elif selected_button == 2 :  # Quit
                            pygame.quit()
                            exit()
                        elif event.key == pygame.K_ESCAPE :
                                show_option_screen = False
                                show_menu_screen = True
                    elif show_option_screen :
                        if selected_button == 1 :  # Controls
                            show_menu_screen = False
                            show_option_screen = False
                            show_controls_screen = True
                        elif selected_button == 2 :  # Volume
                            show_menu_screen = False
                            show_option_screen = False
                            show_volume_screen = True
                    elif show_controls_screen : # YongXin Part
                        if event.key == pygame.K_ESCAPE :
                            show_controls_screen = False
                            show_option_screen = True  # Navigate from controls to option
                    elif show_volume_screen :
                        if selected_button == 1 :  # On sound
                            pygame.mixer.music.play()
                        elif selected_button == 2 :  # Off sound
                            pygame.mixer.music.stop()
                        elif event.key == pygame.K_ESCAPE : # YongXin Part
                            if show_option_screen :
                                show_option_screen = False
                                show_menu_screen = True  # Navigate from volume to option
                            elif show_menu_screen :
                                show_menu_screen = False
                                show_volume_screen = False  # Navigate from option to menu
                    elif show_game_screen :
                        if event.key == pygame.K_ESCAPE :
                            show_game_screen = False
                            show_menu_screen = True 
                            
                elif event.key == pygame.K_DOWN : # Basic scrollig through the menu
                    if show_menu_screen :
                        if selected_button < 2 :
                            selected_button += 1
                    if show_option_screen :
                        selected_button = 1
                        if selected_button <= 2 :
                            selected_button += 1
                    if show_volume_screen :
                        selected_button = 1
                        if selected_button <= 2 :
                            selected_button += 1
                elif event.key == pygame.K_UP :
                    if show_menu_screen :
                        if selected_button > 0 :
                            selected_button -= 1
                    if show_option_screen :
                        selected_button = 1
                        if selected_button > 1 :
                            selected_button -= 1
                    if show_volume_screen :
                        selected_button = 1
                        if selected_button > 1 :
                            selected_button -= 1
                elif event.key == pygame.K_ESCAPE : # YongXin Part
                    if show_option_screen :
                        show_option_screen = False
                        show_menu_screen = True  # Navigate from option to menu
                    elif show_controls_screen :
                        show_controls_screen = False
                        show_option_screen = True # Navigate from controls to option
                    elif show_volume_screen :
                        show_volume_screen = False
                        show_option_screen = True  # Navigate from volume to option
                    elif show_game_screen :
                        show_game_screen = False
                        show_menu_screen = True 
if __name__ == "__main__" :
    pygame.init()
    pygame.display.set_caption("Duck In Danger!")
    WIDTH, HEIGHT =(1600, 1000)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    main(screen)
