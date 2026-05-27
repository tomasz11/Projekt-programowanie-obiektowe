import pygame
from map import Map
from player import Player
from bullet import Bullet
from menu import Button

# Stany gry
MENU = 0
GAME = 1
PICK_PLAYER = 2
SETTINGS = 3

current_state = MENU
resolution = (1280, 700)
pygame.init()
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("uwu")
clock = pygame.time.Clock()

# Inicjalizacja obiektów
my_map = Map()
my_player = Player(40, 40)
bullets = []

# Przyciski menu
btn_start = Button(540, 200, 200, 60, "START GAME")
btn_pick  = Button(540, 300, 200, 60, "PICK PLAYER")
btn_settings = Button(540, 400, 200, 60, "SETTINGS")

running = True
while running:
    # 1. OBSŁUGA ZDARZEŃ (EVENTS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            
        if current_state == MENU:
            if btn_start.is_clicked(event):
                current_state = GAME
            if btn_pick.is_clicked(event):
                current_state = PICK_PLAYER
            if btn_settings.is_clicked(event):
                current_state = SETTINGS
        
        elif current_state == GAME:
            # Strzelanie tylko gdy trwa gra!
            if event.type == pygame.MOUSEBUTTONDOWN:
                angle = my_player.get_angle()
                new_bullet = Bullet(my_player.rect.centerx, my_player.rect.centery, angle)
                bullets.append(new_bullet)

        # Powrót do menu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                current_state = MENU

    # 2. LOGIKA GRY (Tylko gdy current_state == GAME)
    if current_state == GAME:
        walls = my_map.get_wall_rects()
        my_player.movement(walls)

        for bullet in bullets[:]:
            bullet.update()
            # Usuwanie pocisków poza ekranem
            if bullet.pos.x < 0 or bullet.pos.x > 1280 or bullet.pos.y < 0 or bullet.pos.y > 700:
                bullets.remove(bullet)
                continue
            # Kolizje pocisków ze ścianami
            for wall in walls:
                if wall.collidepoint(bullet.pos):
                    if bullet in bullets:
                        bullets.remove(bullet)
                    break

    # 3. RYSOWANIE (RENDERING)
    screen.fill((30, 30, 30)) # Czyścimy ekran raz

    if current_state == MENU:
        btn_start.draw(screen)
        btn_pick.draw(screen)
        btn_settings.draw(screen)
        
    elif current_state == GAME:
        my_map.draw(screen)
        my_player.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        
    elif current_state == PICK_PLAYER:
        msg = pygame.font.SysFont('Arial', 50).render("Select Your Character", True, (255, 255, 255))
        screen.blit(msg, (400, 300))
        
    elif current_state == SETTINGS:
        msg = pygame.font.SysFont('Arial', 50).render("Settings Menu", True, (255, 255, 255))
        screen.blit(msg, (500, 300))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()