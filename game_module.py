import pygame
from animation import AnimationController


#MAIN
def start_button(screen):
    start_button_rect = pygame.Rect(740, 350,200,100)
    pygame.draw.rect(screen, (0, 0, 0), start_button_rect)
    font_size = 72
    font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf",font_size)
    text = font_name.render("Start", True, (255, 255, 255))
    text_rect = text.get_rect(center=start_button_rect.center)
    screen.blit(text, text_rect)
    
def option_button(screen):
    option_button_rect = pygame.Rect(740, 450, 200, 100)
    pygame.draw.rect(screen, (0, 0, 0), option_button_rect)
    font_size = 72
    font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf",font_size)
    text = font_name.render("Option", True, (255, 255, 255))
    text_rect = text.get_rect(center=option_button_rect.center)
    screen.blit(text, text_rect)
    
def quit_button(screen):
    quit_button_rect = pygame.Rect(740, 550, 200, 100)
    pygame.draw.rect(screen, (0, 0, 0), quit_button_rect)
    font_size = 72
    font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf",font_size)
    text = font_name.render("Quit", True, (255, 255, 255))
    text_rect = text.get_rect(center=quit_button_rect.center)
    screen.blit(text, text_rect)
    
def resume_button(screen):
    resume_button_rect = pygame.Rect(740, 650, 200, 100)
    pygame.draw.rect(screen, (0, 0, 0), resume_button_rect)
    font_size = 72
    font_name = pygame.font.Font("fonts/8-BIT WONDER.ttf",font_size)
    text = font_name.render("Resume", True, (255, 255, 255))
    text_rect = text.get_rect(center=resume_button_rect.center)
    screen.blit(text, text_rect)


def main(screen):
    clock = pygame.time.Clock()

    animation_controller = AnimationController()

    show_home_screen = True
    selected_button = 0  # 0 is start, 1 is option, 2 is  quit 

    selected_button_blink_timer = 0
    selected_button_blink_cooldown = 350
    is_button_visible = True
    
    run = True
    while run:
        clock.tick(60)

        screen.fill((0, 0, 0))

        if show_home_screen:
            start_button(screen)
            option_button(screen)
            quit_button(screen)
            selected_button_blink_timer += clock.get_time()
            
            if selected_button_blink_timer >= selected_button_blink_cooldown:
                selected_button_blink_timer = 0
                is_button_visible = not is_button_visible
            if is_button_visible:
                selection_button = pygame.Rect(540, 350 + selected_button * 100, 30, 100)
                pygame.draw.rect(screen, (255, 255, 255), selection_button)
        else:
            screen.blit(pygame.image.load("graphics/background1.png"), (0, 0))
            animation_controller.update_animation(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                if show_home_screen and event.key == pygame.K_RETURN:
                    if selected_button == 0:  #start game
                        show_home_screen = False  
                        animation_controller.setup_animation()
                    if selected_button == 1: #option
                        pass 
                    if selected_button == 2: #quit
                        pygame.quit()
                        exit()
                elif event.key == pygame.K_DOWN:
                    if selected_button < 2:
                        selected_button += 1
                elif event.key == pygame.K_UP:
                    if selected_button > 0:
                        selected_button -= 1

    pygame.quit()
    exit()