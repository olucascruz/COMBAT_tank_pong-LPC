import pygame
from game import Game

class main:
    clock = pygame.time.Clock()
    game = Game()
    game.play(clock)
