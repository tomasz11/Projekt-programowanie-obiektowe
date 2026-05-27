import pygame

class Camera:
    def __init__(self, width, height):
        # Rect, który przechowuje przesunięcie świata
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity_rect):
        # Ta funkcja bierze np. Rect gracza i zwraca nowy Rect przesunięty o kamerę
        return entity_rect.move(self.camera.topleft)

    def update(self, target_rect):
        # Obliczamy przesunięcie (środek ekranu - pozycja gracza)
        x = -target_rect.centerx + int(1280 / 2)
        y = -target_rect.centery + int(700 / 2)

        # Blokada kamery, żeby nie wyjeżdżała poza krawędzie mapy
        x = min(0, x)  # lewa krawędź
        y = min(0, y)  # górna krawędź
        x = max(-(self.width - 1280), x) # prawa krawędź
        y = max(-(self.height - 700), y) # dolna krawędź

        self.camera.topleft = (x, y)