import pygame
from parametres import *
import circle_movement
from general_functions import *
from Button import *
from walls import *
from menu import *
from mouse_cursor import *
from load_music import *

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

icon = load_image('icon.jpg')
pygame.display.set_icon(icon)

all_circles = pygame.sprite.Group()
all_obstacles = pygame.sprite.Group()
fps_clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
red_circle = circle_movement.Circles(
    RED_CIRCLE_IMG, RED_CIRCLE_START_ANGLE, RED_CIRCLE_START_X, RED_CIRCLE_START_Y, RED)
blue_circle = circle_movement.Circles(
    BLUE_CIRCLE_IMG, BLUE_CIRCLE_START_ANGLE, BLUE_CIRCLE_START_X, BLUE_CIRCLE_START_Y, BLUE)

all_circles.add(red_circle, blue_circle)
mouse = Mouse()
all_sprites.add(mouse)
scores = 0


def game_over(l_id):
    game_cycle(l_id)


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


def create_obst_group(lev_id):
    group = pygame.sprite.Group()

    twist_walls = get_obstacles(lev_id, TWIST_OBSTACLES)
    for wall in twist_walls:
        wall_sprite = TwistObstacle(*wall)
        wall_sprite.add(group)

    lf_walls = get_obstacles(lev_id, LF_DOWN_OBSTACLES)
    for wall in lf_walls:
        wall_sprite = LfDownObstacle(*wall)
        wall_sprite.add(group)

    side_walls = get_obstacles(lev_id, SIDE_OBSTACLES)
    for wall in side_walls:
        wall_sprite = SlideSideObstacle(*wall)
        wall_sprite.add(group)
    return group


def press_key():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pause()
    if keys[pygame.K_RIGHT]:
        red_circle.update(SPEED_MOVEMENT_TRUE)
        blue_circle.update(SPEED_MOVEMENT_TRUE)
    if keys[pygame.K_LEFT]:
        red_circle.update(SPEED_MOVEMENT_FALSE)
        blue_circle.update(SPEED_MOVEMENT_FALSE)


def game_cycle(l_id):
    pygame.mixer.music.stop()
    game = True
    walls_group = create_obst_group(l_id)
    traces_wall = []
    while game:
        loc_walls_group = pygame.sprite.Group()
        for wall in walls_group:
            if check_sane_y_cord(wall.rect.y):
                wall.add(loc_walls_group)
        for wall in loc_walls_group:
            traces_wall.append(TraceObstacle(*wall.get_trace_inf()))

        for i in range(len(traces_wall) - 1, -1, -1):
            if traces_wall[i].color_rgb == [50, 50, 50]:
                traces_wall.pop(i)

        # pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                quit()
        press_key()

        if any([red_circle.check_collision(screen, walls_group), blue_circle.check_collision(screen, walls_group)]):
            pygame.mixer.Sound.play(sound_collision)
            return game_over(l_id)
        screen.fill(BLACK_COLOR)
        print_text(screen, f'Dodged: {scores}', 10, 10, 20)

        pygame.draw.circle(screen, DEEP_GRAY, GRAY_CIRCLE_POSITION,
                           GRAY_CIRCLE_RADIUS, GRAY_CIRCLE_WIDTH)
        for trace in circle_movement.traces:
            trace.draw(screen)
            trace.update()

        all_circles.draw(screen)
        for i in range(len(traces_wall)):
            traces_wall[i].update_color()
            traces_wall[i].draw_trace(screen)
        walls_group.update()
        loc_walls_group.draw(screen)

        pygame.display.update()
        fps_clock.tick(FPS)


def start_game():
    Menu(SIZE)


if __name__ == '__main__':
    start_game()
