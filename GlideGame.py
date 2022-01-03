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
mouse = Mouse()
all_sprites.add(mouse)
scores = 0
paused = True

# ПРОВЕРКА НА СЛЕДЫ ПОТОМ
red_circle = circle_movement.Circles(
    RED_CIRCLE_IMG, RED_CIRCLE_START_ANGLE, RED_CIRCLE_START_X, RED_CIRCLE_START_Y, RED)
blue_circle = circle_movement.Circles(
    BLUE_CIRCLE_IMG, BLUE_CIRCLE_START_ANGLE, BLUE_CIRCLE_START_X, BLUE_CIRCLE_START_Y, BLUE)


def changing_speed(red, blue, speed, flag, angle_stop_red=None, angle_stop_blue=None):
    if angle_stop_red is None and angle_stop_blue is None:
        if flag:
            red.update(speed)
            blue.update(speed)
        else:
            red.update(speed)
            blue.update(speed)
    else:
        while red.init_angle >= angle_stop_red:
            red.update(-abs(speed))
        while red.init_angle <= angle_stop_red:
            red.update(abs(speed))
        while blue.init_angle >= angle_stop_blue:
            blue.update(-abs(speed))
        while blue.init_angle <= angle_stop_blue:
            blue.update(abs(speed))


def off_pause():
    global paused
    paused = False


def draw_pause():
    screen.fill(BLACK_COLOR)
    btn_pause = Button(screen, 30, 30)
    btn_pause.draw(560, 0, 'II', pause, 30)


def draw_gray_circle():
    pygame.draw.circle(screen, DEEP_GRAY, GRAY_CIRCLE_POSITION,
                       GRAY_CIRCLE_RADIUS, GRAY_CIRCLE_WIDTH)


def game_over(walls_group, l_id, red, blue):
    game = True
    traces_wall = []
    sound_restart.play()
    while game:
        loc_walls_group = get_loc_walls_gr(walls_group)
        traces_wall = get_traces_arr(loc_walls_group, traces_wall)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                quit()
        if max(list(map(lambda x: x.rect.y, walls_group))) < -350:
            game = False
        draw_pause()
        for w_trace in traces_wall:
            w_trace.draw_trace(screen)
        for i in walls_group:
            i.speed_y -= 1.5
        changing_speed(red, blue, 10, True, RED_CIRCLE_START_ANGLE, BLUE_CIRCLE_START_ANGLE)
        draw_gray_circle()
        walls_group.update()
        all_circles.draw(screen)
        draw_traces_for_circles(True, circle_movement.traces)
        loc_walls_group.draw(screen)

        pygame.display.update()
        fps_clock.tick(FPS)
    game_cycle(l_id)


def pause():
    global paused
    btn_resume_game = Button(screen, 150, 50)
    btn_leave_hub = Button(screen, 150, 50)
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.fill(BLACK_COLOR)
        print_text(screen, message='пауза, нажмите Enter, чтобы', x=40, y=300, font_type='font/DroidSansJapanese.ttf')
        keys = pygame.key.get_pressed()
        btn_resume_game.draw(325, 290, 'продолжить', off_pause, 30)
        btn_leave_hub.draw(320, 350, 'выход', start_game, 30, id=SIZE)

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


def get_traces_arr(loc_walls_gr, res):
    for wall in loc_walls_gr:
        res.append(TraceObstacle(*wall.get_trace_inf()))

        for i in range(len(res) - 1, -1, -1):
            if res[i].color_rgb == DELETE_WALL_TRACE_COLOR:
                res.pop(i)
    return res


def press_key(red, blue):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pause()
    if keys[pygame.K_RIGHT]:
        changing_speed(red, blue, SPEED_MOVEMENT_FALSE, True)
    if keys[pygame.K_LEFT]:
        changing_speed(red, blue, SPEED_MOVEMENT_TRUE, False)


def draw_traces_for_circles(flag, traces):
    if flag:
        for trace in traces:
            trace.draw(screen)
            trace.update()


def game_cycle(l_id):
    all_circles.add(red_circle, blue_circle)

    all_circles.add(red_circle, blue_circle)
    pygame.mixer.music.stop()
    game = True
    walls_group = create_obst_group(l_id)
    traces_wall = []
    while game:
        loc_walls_group = get_loc_walls_gr(walls_group)
        traces_wall = get_traces_arr(loc_walls_group, traces_wall)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                quit()
        press_key(red_circle, blue_circle)

        if any([red_circle.check_collision(screen, walls_group), blue_circle.check_collision(screen, walls_group)]):
            pygame.mixer.Sound.play(sound_collision)
            return game_over(walls_group, l_id, red_circle, blue_circle)
        print_text(screen, f'Dodged: {get_dodged(walls_group)}', 10, 10, 20)
        draw_pause()

        # Проверка на нажатие эффектов потом
        draw_traces_for_circles(True, circle_movement.traces)
        draw_gray_circle()

        for w_trace in traces_wall:
            w_trace.draw_trace(screen)
        walls_group.update()
        loc_walls_group.draw(screen)
        all_circles.draw(screen)

        pygame.display.update()
        fps_clock.tick(FPS)


def start_game(screen_size):
    Menu(screen_size)


if __name__ == '__main__':
    start_game(SIZE)
