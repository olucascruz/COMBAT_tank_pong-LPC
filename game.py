import pygame
import config
import bullet
from tank import Tank
from obstacle import Obstacle
from limit import limit_game
from collision import collide, players_collide


# Player Score


class Game:
    def __init__(self):
        self.score_1 = 0
        self.score_2 = 0
        self.pontos1format = None
        self.pontos2format = None

    def play(self, clock):
        pygame.init()
        game_screen = pygame.display.set_mode(config.SCREEN_SIZE)
        pygame.display.set_caption("Tank Pong")
        game_screen.fill(config.RED)

        tank_green = Tank('player_1')
        tank_blue = Tank('player_2')
        obstacle = Obstacle()
        font = pygame.font.Font("font/retro_gaming.ttf", 80)
        key_pressed = set()

        # Creating the player group
        player_1 = pygame.sprite.GroupSingle(tank_green)
        player_2 = pygame.sprite.GroupSingle(tank_blue)

        # Creating the bullets group
        bullets_1 = pygame.sprite.Group()
        bullets_2 = pygame.sprite.Group()

        self.pontos1format = font.render(str(self.score_1), False, config.GREEN)
        self.pontos2format = font.render(str(self.score_2), False, config.BLUE)

        def add_bullet(bullets, player, enemy, num):
            if len(bullets.sprites()) <= config.max_bullets_per_time:
                bullets.add(bullet.Bullet(player.sprite.get_bullet_coordinates(), num, enemy))

        movements = dict(
            forward=lambda: tank_green.move('forward'),
            backward=lambda: tank_green.move('backward'),
            forward2=lambda: tank_blue.move('backward'),
            backward2=lambda: tank_blue.move('forward')
        )

        def move_player():
            for move in key_pressed:
                movements[move]()

        def update_score(player, tank):
            if player == 1:
                self.score_2 = self.score_2 + 1
                tank.hit = False
                self.pontos2format = font.render(str(self.score_2), False, config.BLUE)

            if player == 2:
                self.score_1 = self.score_1 + 1
                tank.hit = False
                self.pontos1format = font.render(str(self.score_1), False, config.GREEN)

        def draw():
            bullets_1.draw(game_screen)
            bullets_1.update()
            bullets_2.draw(game_screen)
            bullets_2.update()

            tank_green.render(game_screen)
            tank_blue.render(game_screen)
            obstacle.render(game_screen)
            limit_game(game_screen)
            game_screen.blit(self.pontos1format, (250, -10))
            game_screen.blit(self.pontos2format, (900, -10))

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

                    # shot
                    if event.key == pygame.K_f:
                        add_bullet(bullets_1, player_1, tank_blue, 1)
                        pygame.time.set_timer(pygame.USEREVENT + 1, 4000)
                    if event.key == pygame.K_RSHIFT:
                        add_bullet(bullets_2, player_2, tank_green, 2)
                        pygame.time.set_timer(pygame.USEREVENT + 2, 4000)

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

            collide(tank_green)
            collide(tank_blue)
            players_collide(tank_green, tank_blue)
            players_collide(tank_blue, tank_green)
            game_screen.fill(config.RED)
            move_player()
            draw()
            pygame.display.update()
