import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.left_obstacle = pygame.image.load("img/defensive_wall.png")
        self.left_obstacle_x = 150
        self.left_obstacle_y = 280
        self.left_obstacle_rect = self.left_obstacle.get_rect()

        self.right_obstacle = pygame.image.load("img/defensive_wall.png")
        self.right_obstacle_rotate = pygame.transform.rotate(self.right_obstacle, 180)
        self.right_obstacle_x = 1000
        self.right_obstacle_y = 280
        self.right_obstacle_rect = self.right_obstacle.get_rect()

        self.horizontal_obstacle = pygame.image.load("img/horizontal_wall.png")
        self.horizontal_obstacle_x = 170
        self.horizontal_obstacle_y = 170
        self.horizontal_obstacle_rect = self.horizontal_obstacle.get_rect()

        self.square_obstacle = pygame.image.load('img/square_wall.png')
        self.square_obstacle_x = 280
        self.square_obstacle_y = 360
        self.square_obstacle_rect = self.square_obstacle.get_rect()

        self.l_obstacle = pygame.image.load('img/L_wall.png')
        self.l_obstacle_x = 400
        self.l_obstacle_y = 490
        self.l_obstacle_rect = self.l_obstacle.get_rect()

        self.l_obstacle2 = pygame.image.load('img/L_wall2.png')
        self.l_obstacle2_x = 720
        self.l_obstacle2_y = 490
        self.l_obstacle2_rect = self.l_obstacle2.get_rect()

    def render(self, surface):
        surface.blit(self.left_obstacle, (self.left_obstacle_x, self.left_obstacle_y))
        surface.blit(self.right_obstacle_rotate, (self.right_obstacle_x, self.right_obstacle_y))

        surface.blit(self.horizontal_obstacle, (self.horizontal_obstacle_x, self.horizontal_obstacle_y))
        surface.blit(self.horizontal_obstacle, (self.horizontal_obstacle_x+770, self.horizontal_obstacle_y))
        surface.blit(self.horizontal_obstacle, (self.horizontal_obstacle_x, self.horizontal_obstacle_y+420))
        surface.blit(self.horizontal_obstacle, (self.horizontal_obstacle_x+770, self.horizontal_obstacle_y+420))

        surface.blit(self.square_obstacle, (self.square_obstacle_x, self.square_obstacle_y))
        surface.blit(self.square_obstacle, (self.square_obstacle_x+600, self.square_obstacle_y))
        surface.blit(self.square_obstacle, (self.square_obstacle_x+300, self.square_obstacle_y+260))
        surface.blit(self.square_obstacle, (self.square_obstacle_x+300, self.square_obstacle_y-255))

        surface.blit(self.l_obstacle, (self.l_obstacle_x, self.l_obstacle_y))
        surface.blit(pygame.transform.rotate(self.l_obstacle, 180),
                     (self.l_obstacle_x+320, self.l_obstacle_y-250))
        surface.blit(self.l_obstacle2, (self.l_obstacle2_x, self.l_obstacle2_y))
        surface.blit(pygame.transform.rotate(self.l_obstacle2, 180),
                     (self.l_obstacle2_x-320, self.l_obstacle2_y-250))
