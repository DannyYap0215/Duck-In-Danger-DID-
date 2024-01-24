import pygame

class SpriteSheet() :
    def __init__(self,image) :
        self.sheet = image
        
    def get_image(self, frame, width, height, scale, colour) : #frame is where the image "start"
        image = pygame.Surface((width,height,)).convert_alpha() # convert_alpha() is used to optimize the image for better performance :P
        image.blit(self.sheet,(0,0), ((frame * width), 0, width, height))   # inserting the image #(image,start from(0,0),start from which frame (frame*width),start from y=0, the rect of width and height)
        image = pygame.transform.scale(image, (width *  scale, height * scale)) # Scales the images
        image.set_colorkey(colour)  #make the colour transparent 
     
        return image