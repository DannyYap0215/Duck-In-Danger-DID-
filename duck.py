import pygame

class DuckSpriteSheet() :
    def __init__(self,image) :
        self.sheet = image
        
    def get_image(self, frame, width, height, scale, colour) :
        image = pygame.Surface((width,height,)).convert_alpha()
        image.blit(self.sheet,(0,0), ((frame * width), 0, width, height))   # inserting the image
        image = pygame.transform.scale(image, (width *  scale, height * scale)) # Scales the images
        image.set_colorkey(colour)  #make the colour transparent 
     
        return image