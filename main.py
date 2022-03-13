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

# Defining the font 
font_1 = pygame.font.Font("font/retro_gaming.ttf", 80)
font_2 = pygame.font.Font("font/retro_gaming.ttf", 80)

# Defining the initial Score
score = 0
score_text = font_1.render(f"{score}", True, "white")
score_text_rect = score_text.get_rect()
score_text_rect.midleft = (300, -40)

# Defining the initial Score
score_2 = 0
score_text_2 = font_2.render(f"{score}", True, "white")
score_text_rect_2 = score_text_2.get_rect()
score_text_rect.midleft = (900, 40)

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
                collision_sound.play()
            if event.key == pygame.K_RSHIFT:
                add_bullet_2.play()

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

        # Check collision between bullet and tank green,
        # and kills them both if they collide
        def bullet_obstacle_collide():
            for bullet in bullets.sprites():
                collision = pygame.sprite.spritecollide(bullet, tank_green, True)

            if collision:
                bullet.kill()
                tank_green.kill()
                update_score_1()
                shot_sound.play()

        # Update score
        def update_score_1():
            global score_text, score, score_text_rect

            score += 1
            score_text = font_1.render(f"{score}", True, "white")
            score_text_rect = score_text.get_rect()
            score_text_rect.midleft = (300, -40)

        # Check collision between bullet and tank blue,
        # and kills them both if they collide
        def bullet_obstacle_collide():
            for bullet in bullets.sprites():
                collision = pygame.sprite.spritecollide(bullet, tank_blue, True)

            if collision:
                bullet.kill()
                tank_blue.kill()
                update_score_2()
                shot_sound.play()

        # Update score
        def update_score_2():
            global score_text, score, score_text_rect

            score += 1
            score_text = font_2.render(f"{score}", True, "white")
            score_text_rect = score_text.get_rect()
            score_text_rect.midleft = (900, 40)

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

    # Score
    game_screen.blit(score_text, score_text_rect)

    # Score
    game_screen.blit(score_text_2, score_text_rect_2)

    limit_game(game_screen)

    pygame.display.update()
