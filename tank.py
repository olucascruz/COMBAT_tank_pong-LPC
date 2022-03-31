import pygame
import config


class Tank(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.speed = config.PLAYER_SPEED
        self.direction = 0
        self.angle = 30
        self.height = 49
        self.width = 52
        self.hit = False

        if self.name == 'player_1':
            self.position_x = config.player_1_starting_position_x
            self.position_y = config.player_1_starting_position_y
            self.image = pygame.image.load("img/tank_green.png").convert_alpha()

        elif self.name == 'player_2':
            self.position_x = config.player_2_starting_position_x
            self.position_y = config.player_2_starting_position_y
            self.image = pygame.image.load("img/tank_blue.png").convert_alpha()

        self.the_rect = self.image.get_rect(center=(self.position_x, self.position_y))

    def rotate(self, rotation_direction):
        if self.direction >= 360 or self.direction <= -360:
            self.direction = 0
        if rotation_direction == 'clockwise':
            self.direction += self.angle
        elif rotation_direction == 'counter-clockwise':
            self.direction -= self.angle

    def move(self, direction_move):
        if self.direction == 360 or self.direction == -360:
            self.direction = 0
        # move right
        vector_move = [(self.speed, 0), (self.speed, -self.speed/2),
                       (self.speed/2, -self.speed), (0, -self.speed),
                       (-self.speed/2, -self.speed), (-self.speed, -self.speed/2)]
        possibles_direction = [0, 30, 60, 90, 120, 150]

        if direction_move == "forward":
            for i in range(len(possibles_direction)):
                if self.direction == possibles_direction[i]:
                    self.position_x += vector_move[i][0]
                    self.position_y += vector_move[i][1]

                elif self.direction == possibles_direction[i]*-1:
                    self.position_x += vector_move[i][0]
                    self.position_y -= vector_move[i][1]

                elif self.direction == possibles_direction[i] + 180:
                    self.position_x -= vector_move[i][0]
                    self.position_y -= vector_move[i][1]

                elif self.direction == (possibles_direction[i] + 180)*-1:
                    self.position_x -= vector_move[i][0]
                    self.position_y += vector_move[i][1]

        elif direction_move == "backward":
            for i in range(len(possibles_direction)):
                if self.direction == possibles_direction[i]:
                    self.position_x -= vector_move[i][0]
                    self.position_y -= vector_move[i][1]

                elif self.direction == possibles_direction[i]*-1:
                    self.position_x -= vector_move[i][0]
                    self.position_y += vector_move[i][1]

                elif self.direction == possibles_direction[i] + 180:
                    self.position_x += vector_move[i][0]
                    self.position_y += vector_move[i][1]

                elif self.direction == (possibles_direction[i] + 180)*-1:
                    self.position_x += vector_move[i][0]
                    self.position_y -= vector_move[i][1]

        self.the_rect.center = [self.position_x, self.position_y]

    def render(self, surface):
        surface.blit(pygame.transform.rotate(self.image, self.direction),
                     (self.position_x, self.position_y))

    def get_bullet_coordinates(self):
        return [self.the_rect.bottomright, self.direction]
