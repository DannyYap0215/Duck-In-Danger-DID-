import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color): #frame is where the image "start"
        frame_x = frame * width # starting position of the image getting "cropped"
        source_rect = pygame.Rect(frame_x, 0, width, height) 
        image = self.sheet.subsurface(source_rect) #makes a new surface of what we need from our spritesheet
        
        scaled_width = int(width * scale) #get scaled width
        scaled_height = int(height * scale) #get scaled height
        image = pygame.transform.scale(image, (scaled_width, scaled_height)) # Scales the images
        
        image.set_colorkey(color) #make the colour transparent 
        
        return image
