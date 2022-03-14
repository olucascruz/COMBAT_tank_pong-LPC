import config
from wall import Wall

wall = Wall()


def collide(player):
    # collision left
    if player.position_x <= 25:
        player.position_x = 25
    # collision up
    if player.position_y <= 105:
        player.position_y = 105
    # collision down
    if player.position_y >= config.SCREEN_HEIGHT - 80:
        player.position_y = config.SCREEN_HEIGHT - 80
    # collision right
    if player.position_x + 80 >= config.SCREEN_WIDTH:
        player.position_x = config.SCREEN_WIDTH - 80
    # collision left wall

    list_y = [wall.left_wall_y, wall.right_wall_y, wall.square_wall_y, wall.l_wall_y, wall.l_wall2_y,
              wall.horizontal_wall_y, wall.horizontal_wall_y, wall.horizontal_wall_y + 420,
              wall.horizontal_wall_y + 420, wall.square_wall_y, wall.square_wall_y + 260,
              wall.square_wall_y - 255, wall.l_wall_y - 250, wall.l_wall_y - 250]

    list_x = [wall.left_wall_x, wall.right_wall_x, wall.square_wall_x, wall.l_wall_x, wall.l_wall2_x,
              wall.horizontal_wall_x, wall.horizontal_wall_x + 770, wall.horizontal_wall_x,
              wall.horizontal_wall_x + 770, wall.square_wall_x + 600, wall.square_wall_x + 300,
              wall.square_wall_x + 300, wall.l_wall_x + 320, wall.l_wall2_x - 320]

    list_rect_h = [wall.left_wall_rect[3], wall.right_wall_rect[3],
                   wall.square_wall_rect[3], wall.l_wall_rect[3], wall.l_wall2_rect[3],
                   wall.horizontal_wall_rect[3], wall.horizontal_wall_rect[3], wall.horizontal_wall_rect[3],
                   wall.horizontal_wall_rect[3], wall.square_wall_rect[3], wall.square_wall_rect[3],
                   wall.square_wall_rect[3], wall.l_wall_rect[3], wall.l_wall_rect[3]]

    list_rect_w = [wall.left_wall_rect[2], wall.right_wall_rect[2],
                   wall.square_wall_rect[2], wall.l_wall_rect[2], wall.l_wall2_rect[2],
                   wall.horizontal_wall_rect[2], wall.horizontal_wall_rect[2], wall.horizontal_wall_rect[2],
                   wall.horizontal_wall_rect[2], wall.square_wall_rect[2], wall.square_wall_rect[2],
                   wall.square_wall_rect[2], wall.l_wall_rect[2], wall.l_wall_rect[2]]

    for i in range(len(list_y)):
        if list_x[i] + 10 >= player.position_x + player.width >= list_x[i] and \
                list_y[i] - 20 < player.position_y + (player.height / 2) < list_y[i] + list_rect_h[i]:
            player.position_x = list_x[i] - player.width

        if list_x[i] + list_rect_w[i] >= player.position_x >= list_x[i] + (list_rect_w[i] - 10) and \
                list_y[i] - 20 < player.position_y + (player.height / 2) < list_y[i] + list_rect_h[i]:
            player.position_x = list_x[i] + list_rect_w[i]

        if list_y[i] + list_rect_h[i] >= player.position_y >= list_y[i] + (list_rect_h[i] - 10) and \
                list_x[i] < player.position_x + (player.width / 2) < list_x[i] + list_rect_w[i]:
            player.position_y = list_y[i] + list_rect_h[i]

        if list_y[i] <= player.position_y + player.height <= list_y[i] + 10 and \
                list_x[i] < player.position_x + (player.width / 2) < list_x[i] + list_rect_w[i]:
            player.position_y = list_y[i] - player.height

    return 0


def players_collide(player1, player2):
    if player2.position_x + 10 >= player1.position_x + player1.width >= player2.position_x and \
            player2.position_y - 20 < player1.position_y + (player1.height / 2) < player2.position_y + player2.height:
        player1.position_x = player2.position_x - player1.width

    if player2.position_x + player2.width >= player1.position_x >= player2.position_x + (player2.width - 10) and \
            player1.position_y - 20 < player1.position_y + (player1.height / 2) < player1.position_y + player2.height:
        player1.position_x = player2.position_x + player2.width

    if player2.position_y + player2.height >= player1.position_y >= player2.position_y + (player2.position_y - 10) and \
            player2.position_x < player1.position_x + (player2.width / 2) < player2.position_x + player2.width:
        player1.position_y = player2.position_y + player2.height

    if player2.position_y <= player1.position_y + player1.height <= player2.position_y + 10 and \
            player2.position_x < player1.position_x + (player1.width / 2) < player2.position_x + player2.width:
        player1.position_y = player2.position_y - player1.height


def collide_bullet(bullet):
    # collision left
    if bullet.rect.x <= 25:
        bullet.dx *= -1
    # collision up
    if bullet.rect.y <= 105:
        bullet.dy *= -1
    # collision down
    if bullet.rect.y >= config.SCREEN_HEIGHT - 25:
        bullet.dy *= -1
    # collision right
    if bullet.rect.x + 80 >= config.SCREEN_WIDTH:
        bullet.dx *= -1
    # collision left wall

    list_y = [wall.left_wall_y, wall.right_wall_y, wall.square_wall_y, wall.l_wall_y, wall.l_wall2_y,
              wall.horizontal_wall_y, wall.horizontal_wall_y, wall.horizontal_wall_y + 420,
              wall.horizontal_wall_y + 420, wall.square_wall_y, wall.square_wall_y + 260,
              wall.square_wall_y - 255, wall.l_wall_y - 250, wall.l_wall_y - 250]

    list_x = [wall.left_wall_x, wall.right_wall_x, wall.square_wall_x, wall.l_wall_x, wall.l_wall2_x,
              wall.horizontal_wall_x, wall.horizontal_wall_x + 770, wall.horizontal_wall_x,
              wall.horizontal_wall_x + 770, wall.square_wall_x + 600, wall.square_wall_x + 300,
              wall.square_wall_x + 300, wall.l_wall_x + 320, wall.l_wall2_x - 320]

    list_rect_h = [wall.left_wall_rect[3], wall.right_wall_rect[3],
                   wall.square_wall_rect[3], wall.l_wall_rect[3], wall.l_wall2_rect[3],
                   wall.horizontal_wall_rect[3], wall.horizontal_wall_rect[3], wall.horizontal_wall_rect[3],
                   wall.horizontal_wall_rect[3], wall.square_wall_rect[3], wall.square_wall_rect[3],
                   wall.square_wall_rect[3], wall.l_wall_rect[3], wall.l_wall_rect[3]]

    list_rect_w = [wall.left_wall_rect[2], wall.right_wall_rect[2],
                   wall.square_wall_rect[2], wall.l_wall_rect[2], wall.l_wall2_rect[2],
                   wall.horizontal_wall_rect[2], wall.horizontal_wall_rect[2], wall.horizontal_wall_rect[2],
                   wall.horizontal_wall_rect[2], wall.square_wall_rect[2], wall.square_wall_rect[2],
                   wall.square_wall_rect[2], wall.l_wall_rect[2], wall.l_wall_rect[2]]

    for i in range(len(list_y)):
        if list_x[i] + 10 >= bullet.rect.x + bullet.width >= list_x[i] and \
                list_y[i] - 20 < bullet.rect.y + (bullet.height / 2) < list_y[i] + list_rect_h[i]:
            bullet.dx *= -1
            bullet.dy += -0.75

        if list_x[i] + list_rect_w[i] >= bullet.rect.x >= list_x[i] + (list_rect_w[i] - 10) and \
                list_y[i] - 20 < bullet.rect.y + (bullet.height / 2) < list_y[i] + list_rect_h[i]:
            bullet.dx *= -1
            bullet.dy += -0.75

        if list_y[i] + list_rect_h[i] >= bullet.rect.y >= list_y[i] + (list_rect_h[i] - 10) and \
                list_x[i] < bullet.rect.x + (bullet.width / 2) < list_x[i] + list_rect_w[i]:
            bullet.dy *= -1
            bullet.dx += -0.75

        if list_y[i] <= bullet.rect.y + bullet.height <= list_y[i] + 10 and \
                list_x[i] < bullet.rect.x + (bullet.width / 2) < list_x[i] + list_rect_w[i]:
            bullet.dy *= -1
            bullet.dx += -0.75
