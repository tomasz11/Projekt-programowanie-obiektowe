import pygame

class Map:
    def __init__(self):
        self.matrix = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
            [1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1],
            [1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ]
        self.block_size = 40
        bajoro = ["lewyg_bajoro.png"]

        self.wall_texture = pygame.image.load("blok.png").convert_alpha()

        self.wall_texture = pygame.transform.scale(self.wall_texture, (self.block_size, self.block_size))
        
        self.wall_texture_bajoro = pygame.image.load(bajoro[0]).convert_alpha()
        self.wall_texture_bajoro = pygame.transform.scale(self.wall_texture_bajoro, (self.block_size, self.block_size))
        self.wall_texture_bajoro_rotated_1 = pygame.transform.rotate(self.wall_texture_bajoro, 90)
        self.wall_texture_bajoro_rotated_1 = pygame.transform.scale(self.wall_texture_bajoro_rotated_1, (self.block_size, self.block_size))
        self.wall_texture_bajoro_rotated_2 = pygame.transform.rotate(self.wall_texture_bajoro, 180)
        self.wall_texture_bajoro_rotated_2 = pygame.transform.scale(self.wall_texture_bajoro_rotated_2, (self.block_size, self.block_size))
        self.wall_texture_bajoro_rotated = pygame.transform.rotate(self.wall_texture_bajoro, 270)
        self.wall_texture_bajoro_rotated = pygame.transform.scale(self.wall_texture_bajoro_rotated, (self.block_size, self.block_size))



    def draw(self, screen):
        for row_index, row in enumerate(self.matrix):
            for col_index, tile in enumerate(row):
                if tile == 1:
                    x = col_index * self.block_size
                    y = row_index * self.block_size
                    screen.blit(self.wall_texture, (x, y))
        

        screen.blit(self.wall_texture_bajoro, (120, 120))
        screen.blit(self.wall_texture_bajoro_rotated, (160, 120))
        screen.blit(self.wall_texture_bajoro_rotated_1, (120, 160))
        screen.blit(self.wall_texture_bajoro_rotated_2, (160, 160))




    def get_wall_rects(self):
        wall_rects = []
        for row_index, row in enumerate(self.matrix):
            for col_index, tile in enumerate(row):
                if tile == 1:
                    x = col_index * self.block_size
                    y = row_index * self.block_size
                    wall_rects.append(pygame.Rect(x, y, self.block_size, self.block_size))
        return wall_rects