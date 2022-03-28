import pygame
import config
import bullet
from tank import Tank
from obstacle import Obstacle
from limit import limit_game
from collision import collide, players_collide

# Player Score
score_1 = 0
score_2 = 0

Mens_pontos1format = None
Mens_pontos2format = None


def game():
    global Mens_pontos1format, Mens_pontos2format
    global score_1, score_2

    pygame.init()

    game_screen = pygame.display.set_mode(config.SCREEN_SIZE)
    pygame.display.set_caption("Tank Pong")
    game_screen.fill(config.RED)

    tank_green = Tank('player_1')
    tank_blue = Tank('player_2')
    obstacle = Obstacle()
    clock = pygame.time.Clock()

    font = pygame.font.Font("font/retro_gaming.ttf", 80)
    Mens_pontos1format = font.render(str(score_1), False, config.GREEN)
    Mens_pontos2format = font.render(str(score_2), False, config.BLUE)
    key_pressed = set()

    def update_score(player, tank):
        global Mens_pontos2format, score_2
        if player == 1:
            score_2 = score_2 + 1
            tank.hit = False
            Mens_pontos2format = font.render(str(score_2), False, config.BLUE)
            
        if player == 2:
            global Mens_pontos1format, score_1
            score_1 = score_1 + 1
            tank.hit = False
            Mens_pontos1format = font.render(str(score_1), False, config.GREEN)

    # Creating the player group
    player_1 = pygame.sprite.GroupSingle(tank_green)
    player_2 = pygame.sprite.GroupSingle(tank_blue)

    # Creating the bullets group
    bullets_1 = pygame.sprite.Group()
    bullets_2 = pygame.sprite.Group()

    # Shoots a bullet, but there's a maximum
    # of "max_bullets_per_time" bullets on the screen
    def add_bullet_1():

        if len(bullets_1.sprites()) <= config.max_bullets_per_time:
            bullets_1.add(bullet.Bullet(player_1.sprite.get_bullet_coordinates(), 1, tank_blue))

    def add_bullet_2():

        if len(bullets_2.sprites()) <= config.max_bullets_per_time:
            bullets_2.add(bullet.Bullet(player_2.sprite.get_bullet_coordinates(), 2, tank_green))

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
                    pygame.time.set_timer(pygame.USEREVENT + 1, 4000)
                if event.key == pygame.K_RSHIFT:
                    add_bullet_2()
                    pygame.time.set_timer(pygame.USEREVENT + 2, 4000)
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

            if event.type == pygame.USEREVENT + 1:
                if len(bullets_1.sprites()) >= config.max_bullets_per_time:
                    for i in bullets_1:
                        i.kill()
                    
            if event.type == pygame.USEREVENT + 2:
                if len(bullets_1.sprites()) >= config.max_bullets_per_time:
                    for i in bullets_2:
                        i.kill()

            # Check if the user wants to exit
            if event.type == pygame.QUIT:
                pygame.quit()

        if tank_green.hit:
            update_score(1, tank_green)
            for i in bullets_2:
                i.kill()
                config.shot_sound.play()

        if tank_blue.hit:
            update_score(2, tank_blue)
            for i in bullets_1:
                i.kill()
                config.shot_sound.play()

        move_player()

        # Drawing the elements on the screen
        game_screen.fill(config.RED)

        bullets_1.draw(game_screen)
        bullets_1.update()

        bullets_2.draw(game_screen)
        bullets_2.update()

        tank_green.render(game_screen)
        tank_blue.render(game_screen)
        obstacle.render(game_screen)

        collide(tank_green)
        collide(tank_blue)
        players_collide(tank_green, tank_blue)
        players_collide(tank_blue, tank_green)

        # Shows Score
        game_screen.blit(Mens_pontos1format, (250, -10))
        game_screen.blit(Mens_pontos2format, (900, -10))

        limit_game(game_screen)

        pygame.display.update()
