# import pygame
# from parametres import *
import circle_movement
# from general_functions import *
# from Button import *
from walls import *
# import time
from menu import *

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

icon = load_image('icon.png')
pygame.display.set_icon(icon)

all_circles = pygame.sprite.Group()
all_obstacles = pygame.sprite.Group()
fps_clock = pygame.time.Clock()

red_circle = circle_movement.Circles(
    RED_CIRCLE_IMG, RED_CIRCLE_START_ANGLE, RED_CIRCLE_START_X, RED_CIRCLE_START_Y, RED)
blue_circle = circle_movement.Circles(
    BLUE_CIRCLE_IMG, BLUE_CIRCLE_START_ANGLE, BLUE_CIRCLE_START_X, BLUE_CIRCLE_START_Y, BLUE)

all_circles.add(red_circle, blue_circle)

level_id = 1
scores = 0

lf_down_walls = pygame.sprite.Group()
# all_walls = get_obstacles(level_id, LF_DOWN_OBSTACLES)
all_walls = get_obstacles(level_id, SIDE_OBSTACLES)


# print(all_walls)

def game_over():
    global scores
    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        print_text(screen, 'Game over. Press Enter to play again, Esc to return to the menu', 20, 300, 15)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return True
        if keys[pygame.K_ESCAPE]:
            return False
        scores = 0

        pygame.display.update()
        fps_clock.tick(15)


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        print_text(screen, 'Paused. Press enter to continue', 30, 300)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False
        pygame.display.update()
        fps_clock.tick(15)


def create_obstacle(ws_arr):
    for i in range(len(ws_arr)):
        ws_arr[i][1][INX_Y_POS] = ws_arr[i][1][INX_Y_POS] + ws_arr[i][1][INX_Y_SPEED]
        ws_arr[i][1][INX_X_POS] = ws_arr[i][1][INX_X_POS] + ws_arr[i][1][INX_X_SPEED]
        if ws_arr[i][1][INX_Y_POS] >= -200 and ws_arr[i][INX_INVIZ]:
            ws_arr[i][INX_INVIZ] = False
            # print(*ws_arr[i][1])
            # wall = LfDownObstacle(*ws_arr[i][1])
            wall = SlideSideObstacle(*ws_arr[i][1])
            wall.add(lf_down_walls)


def delete_obstacle(walls_list):
    global scores
    for enemy in walls_list:
        if enemy.rect.y > 800:
            walls_list.remove(enemy)
            scores += 1


def press_key():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pause()
    if keys[pygame.K_RIGHT]:
        red_circle.update(SPEED_MOVEMENT_FALSE)
        blue_circle.update(SPEED_MOVEMENT_FALSE)
    if keys[pygame.K_LEFT]:
        red_circle.update(SPEED_MOVEMENT_TRUE)
        blue_circle.update(SPEED_MOVEMENT_TRUE)


def game_cycle():
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        press_key()

        if any([red_circle.check_collision(screen, lf_down_walls), blue_circle.check_collision(screen, lf_down_walls)]):
            return game_over()

        screen.fill(BLACK_COLOR)
        print_text(screen, f'Dodged: {scores}', 10, 10, 20)

        create_obstacle(all_walls)
        delete_obstacle(lf_down_walls)

        pygame.draw.circle(screen, DEEP_GRAY, GRAY_CIRCLE_POSITION,
                           GRAY_CIRCLE_RADIUS, GRAY_CIRCLE_WIDTH)
        for trace in circle_movement.traces:
            trace.draw(screen)
            trace.update()

        all_circles.draw(screen)

        lf_down_walls.update()
        lf_down_walls.draw(screen)

        pygame.display.update()
        fps_clock.tick(FPS)
    return game_over()


# СТАРОЕ МЕНЮ
# def show_menu():
#     menu_background = load_image('menu.png')
#     start_btn = Button(screen, 300, 70)
#     quit_btn = Button(screen, 300, 70)
#     showing = True
#     while showing:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#         screen.blit(menu_background, (0, 0))
#         start_btn.draw(150, 200, 'Start game', start_game, 40)
#         quit_btn.draw(150, 300, 'Quit game', quit, 40)
#         pygame.display.update()
#         fps_clock.tick(60)


def start_game():
    # global scores
    while game_cycle():
        pass


menu = Menu((600, 800), game_cycle)

# Вызов старого меню
# show_menu()
