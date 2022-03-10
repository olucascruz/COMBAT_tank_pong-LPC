import pygame
import config


class Tank:
    def __init__(self, name):
        self.name = name

        if self.name == 'player_1':
            self.image = pygame.image.load("img/tank_green.png")
            self.position_x = config.player_1_starting_position_x
            self.position_y = config.player_1_starting_position_y

        elif self.name == 'player_2':
            self.image = pygame.image.load("img/tank_blue.png")
            self.position_x = config.player_2_starting_position_x
            self.position_y = config.player_2_starting_position_y

    def render(self, surface):
        surface.blit(self.image, (self.position_x, self.position_y));
