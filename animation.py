import pygame
import spritesheet

class AnimationController():
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.animation_list = []
        self.action = 0
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 200  # speed

    def setup_animation(self):
        duck_sprite_sheet_image = pygame.image.load("graphics/white-duck/white-duck-walk.png").convert_alpha()
        sprite_sheet = spritesheet.SpriteSheet(duck_sprite_sheet_image)
        
        animation_steps = [3, 5] #3 images for the first animation (frame 0) and 5 images for the second animation (frame 1)
        step_counter = 0

        for animation in animation_steps:
            temp_image_list = []
            for _ in range(animation):
                temp_image_list.append(sprite_sheet.get_image(step_counter, 40, 40, 5, self.BLACK)) #step_counter is the x-cords where the current frame of spritesheet starts #get_image is from spritesheet module where step_counter will be 1, 2, 3 and it will affect which image is gotten :P
                step_counter += 1
            self.animation_list.append(temp_image_list)# so whne starting it append two different animation list into the empty list 

        self.action = 0 
        self.frame = 0
        self.last_update = pygame.time.get_ticks()

    def update_animation(self, screen, player_x, player_y):
        current_time = pygame.time.get_ticks()
        if (current_time - self.last_update) >= self.animation_cooldown: # calculates the time elapsed since the last update between the current time. #example the d animation is at 5 sec while last updt is at 2 sec it will run
            self.frame += 1# increase when it passes 0.2sec
            self.last_update = current_time #update the times
            if self.frame >= len(self.animation_list[self.action]): #check if the frame is equal to or bigger than, meaning the animation frames is finished, if yes then it resets to 0
                self.frame = 0 
                

        # Update the animation every 0.2 sec
        screen.blit(self.animation_list[self.action][self.frame], (player_x, player_y))

