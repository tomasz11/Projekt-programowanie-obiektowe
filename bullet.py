import pygame
import math

class Bullet:
    def __init__(self, x, y, angle):
        self.pos = pygame.math.Vector2(x, y)
        self.speed = 10
        self.velocity = pygame.math.Vector2(math.cos(angle), math.sin(angle)) * self.speed
        self.radius = 5

    def update(self):
        # Move the bullet
        self.pos += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.pos.x), int(self.pos.y)), self.radius)