import pygame
import config
from tank import Tank
from wall import Wall

pygame.init()

game_screen = pygame.display.set_mode(config.SCREEN_SIZE)
pygame.display.set_caption("Tank Pong")
game_screen.fill(config.RED)


tank_pink = Tank('player_1')
tank_white = Tank('player_2')
wall = Wall()
clock = pygame.time.Clock()
# Game_loop
while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    tank_pink.render(game_screen)
    tank_white.render(game_screen)
    wall.render(game_screen)

    pygame.display.update()
