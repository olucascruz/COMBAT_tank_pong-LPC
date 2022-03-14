import pygame
import config
import random
from collision import collide_bullet


class Bullet(pygame.sprite.Sprite):
    def __init__(self, coord, player, enemy):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill("red")

        directions = [30, 60, 210, 240, -120, -150, -300, -330]

        self.direction = coord[1]

        self.player = player

        for direction in directions:
            if direction == self.direction:
                coord[0] = (coord[0][0] + 8, coord[0][1] + 8)
                break

        self.rect = self.image.get_rect(center=coord[0])
        self.speed = 15

        self.dx = 0
        self.dy = 0

        self.set_direction()
        self.position_x = self.rect.x
        self.position_y = self.rect.y
        self.width = 5
        self.height = 5
        self.enemy = enemy

    def movement(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.bottom < 0 or self.rect.top > 700 or self.rect.left > 1200 or self.rect.right < 0:
            self.kill()

    def set_direction(self):
        if self.direction == 0 or self.direction == 360 or self.direction == -360:
            self.dx = -1 * self.speed

        if self.direction == 30 or self.direction == -330:
            self.dx = -1 * self.speed
            self.dy = self.speed/2

        if self.direction == -30 or self.direction == 330:
            self.dx = -1 * self.speed
            self.dy = -1 * (self.speed/2)

        if self.direction == 60 or self.direction == -300:
            self.dx = -1 * (self.speed/2)
            self.dy = self.speed

        if self.direction == -60 or self.direction == 300:
            self.dx = -1 * (self.speed/2)
            self.dy = -1 * self.speed

        if self.direction == 90 or self.direction == -270:
            self.dy = self.speed

        if self.direction == 120 or self.direction == -240:
            self.dx = (self.speed/2)
            self.dy = self.speed

        if self.direction == 150 or self.direction == -210:
            self.dx = self.speed
            self.dy = (self.speed/2)

        if self.direction == 180 or self.direction == -180:
            self.dx = self.speed

        if self.direction == 270 or self.direction == -90:
            self.dy = -1 * self.speed

        if self.direction == -120 or self.direction == 240:
            self.dx = (self.speed/2)
            self.dy = -1 * self.speed

        if self.direction == -150 or self.direction == 210:
            self.dx = self.speed
            self.dy = -1 * (self.speed/2)
        
        if self.player == 1:
            print("2")
            self.dx *= -1
            self.dy *= -1

    def collide_with_tank(self):
        if self.rect.colliderect(self.enemy.the_rect):
            locals_list = [50, 180, 1100, 180, 50, 650, 1100, 650]
            self.enemy.position_x = locals_list[random.randint(0, 7)]
            self.enemy.position_y = locals_list[random.randint(0, 7)]
            self.enemy.hit = True

    def update(self):
        self.movement()
        self.collide_with_tank()
        collide_bullet(self)
