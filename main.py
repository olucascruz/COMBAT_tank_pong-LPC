import pygame
import config
from tank import Tank
from wall import Wall
from limit import limit_game

pygame.init()

game_screen = pygame.display.set_mode(config.SCREEN_SIZE)
pygame.display.set_caption("Tank Pong")
game_screen.fill(config.RED)


tank_green = Tank('player_1')
tank_blue = Tank('player_2')
wall = Wall()
clock = pygame.time.Clock()

key_pressed = set()

movements = dict(
    forward=lambda: tank_green.move('forward'),
    backward=lambda: tank_green.move('backward'),
    forward2=lambda: tank_blue.move('backward'),
    backward2=lambda: tank_blue.move('forward')
)


def move_player():
    for move in key_pressed:
        movements[move]()


# Game_loop
while True:
    clock.tick(16)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                tank_green.rotate('clockwise')
            elif event.key == pygame.K_d:
                tank_green.rotate('counter-clockwise')
            if event.key == pygame.K_w:
                key_pressed.add('forward')
            elif event.key == pygame.K_s:
                key_pressed.add('backward')

            if event.key == pygame.K_LEFT:
                tank_blue.rotate('clockwise')
            elif event.key == pygame.K_RIGHT:
                tank_blue.rotate('counter-clockwise')
            if event.key == pygame.K_UP:
                key_pressed.add('forward2')
            elif event.key == pygame.K_DOWN:
                key_pressed.add('backward2')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                key_pressed.remove('forward')
            elif event.key == pygame.K_s:
                key_pressed.remove('backward')
            if event.key == pygame.K_UP:
                key_pressed.remove('forward2')
            elif event.key == pygame.K_DOWN:
                key_pressed.remove('backward2')

    move_player()

    game_screen.fill(config.RED)

    tank_green.render(game_screen)
    tank_blue.render(game_screen)
    wall.render(game_screen)

    limit_game(game_screen)

    pygame.display.update()
