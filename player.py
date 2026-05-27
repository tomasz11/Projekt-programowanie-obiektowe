import pygame
import math

class Player:
    def __init__(self, x, y):
        
        
        skins = ["ninja.png","john.png"]
        self.original_image = pygame.image.load(skins[1]).convert_alpha()
        
        
        self.image = pygame.transform.scale(self.original_image, (50,80))
        
        
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 4

    def movement(self, walls):
        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_a]: self.rect.x -= self.speed
        for wall in walls:
            if self.rect.colliderect(wall): self.rect.left = wall.right
        
        if keys[pygame.K_d]: self.rect.x += self.speed
        for wall in walls:
            if self.rect.colliderect(wall): self.rect.right = wall.left

        
        if keys[pygame.K_w]: self.rect.y -= self.speed
        for wall in walls:
            if self.rect.colliderect(wall): self.rect.top = wall.bottom
        
        if keys[pygame.K_s]: self.rect.y += self.speed
        for wall in walls:
            if self.rect.colliderect(wall): self.rect.bottom = wall.top

    def draw(self, screen):
    
        mouse_x = pygame.mouse.get_pos()[0]
        if mouse_x < self.rect.centerx:
           
            flipped_image = pygame.transform.flip(self.image, True, False)
            screen.blit(flipped_image, self.rect)
        else:
            screen.blit(self.image, self.rect)


        mouse_pos = pygame.mouse.get_pos()
        start_pos = self.rect.center
        dx = mouse_pos[0] - start_pos[0]
        dy = mouse_pos[1] - start_pos[1]
        angle = math.atan2(dy, dx)
        
        gun_length = 20
        end_pos = (
            start_pos[0] + math.cos(angle) * gun_length,
            start_pos[1] + math.sin(angle) * gun_length
        )
        pygame.draw.line(screen, (128, 108, 108), start_pos, end_pos, 5)

    def get_angle(self):
        mouse_pos = pygame.mouse.get_pos()
        start_pos = self.rect.center
        dx = mouse_pos[0] - start_pos[0]
        dy = mouse_pos[1] - start_pos[1]
        return math.atan2(dy, dx)