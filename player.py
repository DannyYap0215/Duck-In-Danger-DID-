import pygame
from spritesheet import SpriteSheet
from animation import AnimationController

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.animation_controller = AnimationController()
        self.animation_controller.setup_animation()

    def control(self, keys):
        if keys[pygame.K_a]:
            self.x -= self.speed
            self.animation_controller.action = 1  # Set the action for the left movement
        elif keys[pygame.K_d]:
            self.x += self.speed
            self.animation_controller.action = 0  # Set the action for the right movement
        elif keys[pygame.K_w]:
            self.y -= self.speed
            self.animation_controller.action = 2  # Set the action for the up movement
        elif keys[pygame.K_s]:
            self.y += self.speed
            self.animation_controller.action = 3  # Set the action for the down movement
        else:
            self.animation_controller.frame = 0  # Reset frame when not moving

    def draw(self, screen):
        self.animation_controller.update_animation(screen, self.x, self.y)
