import pygame
class Button:
    def __init__(self, x, y, width, height, text, color=(128, 108, 108)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont('Arial', 32)

    def draw(self, screen):
        # Change color slightly when hovering
        mouse_pos = pygame.mouse.get_pos()
        draw_color = (150, 130, 130) if self.rect.collidepoint(mouse_pos) else self.color
        
        pygame.draw.rect(screen, draw_color, self.rect, border_radius=5)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2, border_radius=5) # Border
        
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False