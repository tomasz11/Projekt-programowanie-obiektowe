import pygame

class Camera:
    def __init__(self, width, height):
        
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity_rect):
        
        return entity_rect.move(self.camera.topleft)

    def update(self, target_rect):
        
        x = -target_rect.centerx + int(1280 / 2)
        y = -target_rect.centery + int(700 / 2)

        
        x = min(0, x)  
        y = min(0, y)  
        x = max(-(self.width - 1280), x) 
        y = max(-(self.height - 700), y)

        self.camera.topleft = (x, y)