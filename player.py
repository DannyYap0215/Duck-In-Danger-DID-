# player.py

import pygame
from animation import AnimationController

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.animation_controller = AnimationController()
        self.animation_controller.setup_animation()

    def move_left(self):
        self.x -= self.speed
        self.animation_controller.action = 1  # Set the action for left movement

    def move_right(self):
        self.x += self.speed
        self.animation_controller.action = 0  # Set the action for right movement

    def move_up(self):
        self.y -= self.speed
        self.animation_controller.action = 1  # Set the action for up movement

    def move_down(self):
        self.y += self.speed
        self.animation_controller.action = 1  # Set the action for down movement

    def reset_animation(self):
        self.animation_controller.frame = 0  # Reset frame when not moving

    def draw(self, screen):
        self.animation_controller.update_animation(screen, self.x, self.y)
