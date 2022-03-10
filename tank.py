import pygame
import config


class Tank:
    def __init__(self, name):
        self.name = name
        self.speed = config.PLAYER_SPEED
        self.direction = 0

        if self.name == 'player_1':
            self.image = pygame.image.load("img/tank_green.png")
            self.position_x = config.player_1_starting_position_x
            self.position_y = config.player_1_starting_position_y

        elif self.name == 'player_2':
            self.image = pygame.image.load("img/tank_blue.png")
            self.position_x = config.player_2_starting_position_x
            self.position_y = config.player_2_starting_position_y

    def rotate(self, rotation_direction):
        print(self.direction)
        if self.direction == 360 or self.direction == -360:
            self.direction = 0
        if rotation_direction == 'clockwise':
            self.direction += self.speed
        elif rotation_direction == 'counter-clockwise':
            self.direction -= self.speed

    def move(self, direction_move):
        # move right
        if self.direction == 0 or self.direction == 360 or self.direction == -360:
            if direction_move == 'forward':
                self.position_x += self.speed
            if direction_move == 'backward':
                self.position_x -= self.speed
        if self.direction == 30 or self.direction == -330:
            if direction_move == 'forward':
                self.position_x += self.speed
                self.position_y -= self.speed/2
            if direction_move == 'backward':
                self.position_x -= self.speed
                self.position_y += self.speed/2

        if self.direction == -30 or self.direction == 330:
            if direction_move == 'forward':
                self.position_x += self.speed
                self.position_y += self.speed/2
            if direction_move == 'backward':
                self.position_x -= self.speed
                self.position_y -= self.speed/2

        if self.direction == 60 or self.direction == -300:
            if direction_move == 'forward':
                self.position_x += self.speed/2
                self.position_y -= self.speed
            if direction_move == 'backward':
                self.position_x -= self.speed/2
                self.position_y += self.speed

        if self.direction == -60 or self.direction == 300:
            if direction_move == 'forward':
                self.position_x += self.speed/2
                self.position_y += self.speed
            if direction_move == 'backward':
                self.position_x -= self.speed/2
                self.position_y -= self.speed

        # move up
        if self.direction == 90 or self.direction == -270:
            if direction_move == 'forward':
                self.position_y -= self.speed
            if direction_move == 'backward':
                self.position_y += self.speed

        if self.direction == 120 or self.direction == -240:
            if direction_move == 'forward':
                self.position_x -= self.speed/2
                self.position_y -= self.speed
            if direction_move == 'backward':
                self.position_x += self.speed/2
                self.position_y += self.speed

        if self.direction == 150 or self.direction == -210:
            if direction_move == 'forward':
                self.position_x -= self.speed
                self.position_y -= self.speed/2
            if direction_move == 'backward':
                self.position_x += self.speed
                self.position_y += self.speed/2

        if self.direction == 180 or self.direction == -180:
            if direction_move == 'forward':
                self.position_x -= self.speed
            if direction_move == 'backward':
                self.position_x += self.speed
        if self.direction == 270 or self.direction == -90:
            if direction_move == 'forward':
                self.position_y += self.speed
            if direction_move == 'backward':
                self.position_y -= self.speed

        if self.direction == -120 or self.direction == 240:
            if direction_move == 'forward':
                self.position_x -= self.speed/2
                self.position_y += self.speed
            if direction_move == 'backward':
                self.position_x += self.speed/2
                self.position_y -= self.speed

        if self.direction == -150 or self.direction == 210:
            if direction_move == 'forward':
                self.position_x -= self.speed
                self.position_y += self.speed/2
            if direction_move == 'backward':
                self.position_x += self.speed
                self.position_y -= self.speed/2

    def render(self, surface):
        surface.blit(pygame.transform.rotate(self.image, self.direction),
                     (self.position_x, self.position_y))
