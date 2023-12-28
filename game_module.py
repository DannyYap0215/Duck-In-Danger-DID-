import pygame
from animation import AnimationController
from player import Player

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
    player = Player(400, 300)  # Adjust the initial position as needed
    background = pygame.image.load("graphics/background1.png").convert()

    show_home_screen = True
    selected_button = 0  # 0 is start, 1 is option, 2 is quit

    selected_button_blink_timer = 0
    selected_button_blink_cooldown = 350
    is_button_visible = True

    while True:
        clock.tick(60)

        if show_home_screen:
            screen.fill((0, 0, 0))
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
            # Display the background once and draw the player and animation on top of it
            screen.blit(background, (0, 0))

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                player.move_left()
            elif keys[pygame.K_d]:
                player.move_right()
            elif keys[pygame.K_w]:
                player.move_up()
            elif keys[pygame.K_s]:
                player.move_down()
            else:
                player.reset_animation()

            player.draw(screen)
            player.apply_gravity()
            animation_controller.update_animation(screen, player.x, player.y)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if show_home_screen and event.key == pygame.K_RETURN:
                    if selected_button == 0:  # Start game
                        show_home_screen = False
                        animation_controller.setup_animation()
                    elif selected_button == 1:  # Option
                        pass
                    elif selected_button == 2:  # Quit
                        pygame.quit()
                        exit()
                elif event.key == pygame.K_DOWN:
                    if selected_button < 2:
                        selected_button += 1
                elif event.key == pygame.K_UP:
                    if selected_button > 0:
                        selected_button -= 1

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Duck On The Run!")
    WIDTH, HEIGHT = (1600, 1000)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    main(screen)