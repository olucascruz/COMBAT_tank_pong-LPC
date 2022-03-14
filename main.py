import pygame
import config
import bullet
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

# Players Scores
score_1 = 0
score_2 = 0
font = pygame.font.Font("font/retro_gaming.ttf", 80)
font2 = pygame.font.Font("font/retro_gaming.ttf", 80)
Mens_pontos1 = f'{score_1}'
Mens_pontos1format = font.render(Mens_pontos1, False, config.GREEN)
Mens_pontos2 = f'{score_2}'
Mens_pontos2format = font.render(Mens_pontos2, False, config.BLUE)

def update_score(player):

    if player == 1:
        global score_1, Mens_pontos1, Mens_pontos1format
        score_1 += 1

        Mens_pontos1 = f'{score_1}'
        Mens_pontos1format = font.render(Mens_pontos1, False, config.GREEN)

    if player == 2:
        global score_2, Mens_pontos2, Mens_pontos2format
        score_2 += 1

        Mens_pontos2 = f'{score_2}'
        Mens_pontos2format = font.render(Mens_pontos2, False, config.BLUE)

# Creating the player group
player_1 = pygame.sprite.GroupSingle(tank_green)
player_2 = pygame.sprite.GroupSingle(tank_blue)

# Creating the bullets group
bullets_1 = pygame.sprite.Group()
bullets_2 = pygame.sprite.Group()

# Shoots a bullet, but there's a maximum
# of "max_bullets_per_time" bullets on the screen
def add_bullet_1():
    global bullets

    if len(bullets_1.sprites()) <= config.max_bullets_per_time:
        bullets_1.add(bullet.Bullet(player_1.sprite.get_bullet_coordinates(),1))

def add_bullet_2():
    global bullets

    if len(bullets_2.sprites()) <= config.max_bullets_per_time:
        bullets_2.add(bullet.Bullet(player_2.sprite.get_bullet_coordinates(),2))

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

            if event.key == pygame.K_f:
                add_bullet_1()
                # collision_sound.play()
            if event.key == pygame.K_RSHIFT:
                add_bullet_2()

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

        def bullet_tank_collision():
            collision = pygame.sprite.spritecollide(player_1.sprite,bullets_2,True,pygame.sprite.collide_mask)

            if collision:
                player_1.sprite.death()
                update_score(1)

            collision = pygame.sprite.spritecollide(player_2.sprite,bullets_1,True,pygame.sprite.collide_mask)

            if collision:
                player_2.sprite.death()
                update_score(2)

    move_player()

    # Drawing the elements on the screen
    game_screen.fill(config.RED)

    bullets_1.draw(game_screen)
    bullets_1.update()

    bullets_2.draw(game_screen)
    bullets_2.update()

    tank_green.render(game_screen)
    tank_blue.render(game_screen)
    wall.render(game_screen)

    # Shows Score
    game_screen.blit(Mens_pontos1format,(250,-10))
    game_screen.blit(Mens_pontos2format,(900,-10))

    limit_game(game_screen)

    pygame.display.update()
