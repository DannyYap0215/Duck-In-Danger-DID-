import pygame
from animation import AnimationController

def start_button(screen):
    button_rect = pygame.Rect(screen.get_width() // 2 - 50, screen.get_height() // 2 - 25, 100, 50)
    pygame.draw.rect(screen, (255, 255, 255), button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render("Start", True, (0, 0, 0))
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

def main(screen):
    clock = pygame.time.Clock()

    animation_controller = AnimationController()

    show_home_screen = True

    run = True
    while run:
        clock.tick(60)

        screen.fill((0, 0, 0))  

        if show_home_screen:
            start_button(screen)
        else:
            screen.blit(pygame.image.load("graphics/bg.png"), (0, 0))
            animation_controller.update_animation(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                if show_home_screen and event.key == pygame.K_RETURN:
                    show_home_screen = False  # Transition to animation on Enter key press
                    animation_controller.setup_animation()
                elif event.key == pygame.K_DOWN and animation_controller.action > 0:
                    animation_controller.action -= 1
                    animation_controller.frame = 0
                elif event.key == pygame.K_UP and animation_controller.action < len(animation_controller.animation_list) - 1:
                    animation_controller.action += 1
                    animation_controller.frame = 0

    pygame.quit()
    exit()
