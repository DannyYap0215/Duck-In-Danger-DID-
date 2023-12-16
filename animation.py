import pygame
import spritesheet

class AnimationController:
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.animation_list = []
        self.action = 0
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 150

    def setup_animation(self):
        duck_sprite_sheet_image = pygame.image.load("graphics/white-duck/white-duck-walk.png").convert_alpha()
        sprite_sheet = spritesheet.SpriteSheet(duck_sprite_sheet_image)

        animation_steps = [3, 5]
        step_counter = 0

        for animation in animation_steps:
            temp_image_list = []
            for _ in range(animation):
                temp_image_list.append(sprite_sheet.get_image(step_counter, 40, 40, 5, self.BLACK))
                step_counter += 1
            self.animation_list.append(temp_image_list)

        self.action = 0
        self.frame = 0
        self.last_update = pygame.time.get_ticks()

    def update_animation(self, screen):
        current_time = pygame.time.get_ticks()
        if (current_time - self.last_update) >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation_list[self.action]):
                self.frame = 0

        screen.blit(self.animation_list[self.action][self.frame], (0, 0))
