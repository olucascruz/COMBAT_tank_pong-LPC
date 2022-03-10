import pygame


class Wall:
    def __init__(self):
        self.left_wall = pygame.image.load("img/defensive_wall.png")
        self.left_wall_x = 150
        self.left_wall_y = 290

        self.right_wall = pygame.image.load("img/defensive_wall.png")
        self.right_wall_rotate = pygame.transform.rotate(self.right_wall, 180)
        self.right_wall_x = 1000
        self.right_wall_y = 290

        self.horizontal_wall = pygame.image.load("img/horizontal_wall.png")
        self.horizontal_wall_x = 170
        self.horizontal_wall_y = 180

        self.square_wall = pygame.image.load('img/square_wall.png')
        self.square_wall_x = 280
        self.square_wall_y = 380

    def render(self, surface):
        surface.blit(self.left_wall, (self.left_wall_x, self.left_wall_y))
        surface.blit(self.right_wall_rotate, (self.right_wall_x, self.right_wall_y))

        surface.blit(self.horizontal_wall, (self.horizontal_wall_x, self.horizontal_wall_y))
        surface.blit(self.horizontal_wall, (self.horizontal_wall_x+780, self.horizontal_wall_y))
        surface.blit(self.horizontal_wall, (self.horizontal_wall_x, self.horizontal_wall_y+420))
        surface.blit(self.horizontal_wall, (self.horizontal_wall_x+780, self.horizontal_wall_y+420))

        surface.blit(self.square_wall, (self.square_wall_x, self.square_wall_y))
        surface.blit(self.square_wall, (self.square_wall_x+600, self.square_wall_y))
        surface.blit(self.square_wall, (self.square_wall_x+300, self.square_wall_y+250))
        surface.blit(self.square_wall, (self.square_wall_x+300, self.square_wall_y-250))



