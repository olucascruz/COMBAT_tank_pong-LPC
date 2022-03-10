import pygame
import config

LIMIT_SIZE = 25
LIMIT_COLOR = config.YELLOW


def limit_game(surface):

    limit_left = pygame.draw.rect(surface, LIMIT_COLOR,
                                  pygame.Rect(
                                      0,  # position X
                                      80, # position Y
                                      LIMIT_SIZE,
                                      config.SCREEN_HEIGHT - 80)
                                  )

    limit_up = pygame.draw.rect(surface, LIMIT_COLOR,
                                pygame.Rect(
                                      0,  # position X
                                      80,  # position Y
                                      config.SCREEN_WIDTH,
                                      LIMIT_SIZE)
                                )

    limit_down = pygame.draw.rect(surface, LIMIT_COLOR,
                                  pygame.Rect(
                                       0,  # position X
                                       config.SCREEN_HEIGHT-LIMIT_SIZE,  # position Y
                                       config.SCREEN_WIDTH,
                                       LIMIT_SIZE)
                                 )

    limit_right = pygame.draw.rect(surface, LIMIT_COLOR,
                                   pygame.Rect(
                                        config.SCREEN_WIDTH-LIMIT_SIZE,  # position X
                                        80,  # position Y
                                        LIMIT_SIZE,
                                        config.SCREEN_HEIGHT - 80)
                                    )