import pygame


class Wall:
    def __init__(self):
        self.left_wall = pygame.image.load("img/defensive_wall.png")
        self.left_wall_x = 150
        self.left_wall_y = 280

        self.right_wall = pygame.image.load("img/defensive_wall.png")
        self.right_wall_rotate = pygame.transform.rotate(self.right_wall, 180)
        self.right_wall_x = 1000
        self.right_wall_y = 280

        self.horizontal_wall = pygame.image.load("img/horizontal_wall.png")
        self.horizontal_wall_x = 170
        self.horizontal_wall_y = 170

        self.square_wall = pygame.image.load('img/square_wall.png')
        self.square_wall_x = 280
        self.square_wall_y = 360

        self.l_wall = pygame.image.load('img/L_wall.png')
        self.l_wall_x = 400
        self.l_wall_y = 490

        self.l_wall2 = pygame.image.load('img/L_wall2.png')
        self.l_wall2_x = 720
        self.l_wall2_y = 490

    def render(self, surface):
        surface.blit(self.left_wall, (self.left_wall_x, self.left_wall_y))
        surface.blit(self.right_wall_rotate, (self.right_wall_x, self.right_wall_y))

        surface.blit(self.horizontal_wall, (self.horizontal_wall_x, self.horizontal_wall_y))
        surface.blit(self.horizontal_wall, (self.horizontal_wall_x+770, self.horizontal_wall_y))
        surface.blit(self.horizontal_wall, (self.horizontal_wall_x, self.horizontal_wall_y+420))
        surface.blit(self.horizontal_wall, (self.horizontal_wall_x+770, self.horizontal_wall_y+420))

        surface.blit(self.square_wall, (self.square_wall_x, self.square_wall_y))
        surface.blit(self.square_wall, (self.square_wall_x+600, self.square_wall_y))
        surface.blit(self.square_wall, (self.square_wall_x+300, self.square_wall_y+260))
        surface.blit(self.square_wall, (self.square_wall_x+300, self.square_wall_y-255))

        surface.blit(self.l_wall, (self.l_wall_x, self.l_wall_y))
        surface.blit(pygame.transform.rotate(self.l_wall, 180),
                     (self.l_wall_x+320, self.l_wall_y-250))
        surface.blit(self.l_wall2, (self.l_wall2_x, self.l_wall2_y))
        surface.blit(pygame.transform.rotate(self.l_wall2, 180),
                     (self.l_wall2_x-320, self.l_wall2_y-250))
