import pygame
pygame.mixer.init()


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

GREEN = '#8cc55d'
BLUE = '#3a8ab1'
YELLOW = '#d4a642'
RED = '#90260a'

shot_sound = pygame.mixer.Sound('sound/shot.wav')
collision_sound = pygame.mixer.Sound('sound/beep1.wav')

# defines the max of bullets that can be on the screen at the same time
max_bullets_per_time = 0

player_1_starting_position_x = 50
player_1_starting_position_y = 370
player_2_starting_position_x = 1100
player_2_starting_position_y = 370

PLAYER_SPEED = 10
