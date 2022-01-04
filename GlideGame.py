import pygame
from parametres import *
import circle_movement
from general_functions import *
from Button import *
from walls import *
from menu import *
from mouse_cursor import *
from load_music import *
from cut_sheet import *

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


def start_game(screen_size):
    return Menu(screen_size)


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
        if red.init_angle > angle_stop_red:
            red.update(-abs(speed))
        elif red.init_angle < angle_stop_red:
            red.update(abs(speed))
        if blue.init_angle > angle_stop_blue:
            blue.update(-abs(speed))
        elif blue.init_angle < angle_stop_blue:
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
        draw_traces_for_circles(select_table('settings', 'effects')[0][0], circle_movement.traces)
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
        changing_speed(red, blue, SPEED_MOVEMENT_TRUE, True)
    if keys[pygame.K_LEFT]:
        changing_speed(red, blue, SPEED_MOVEMENT_FALSE, False)


def draw_traces_for_circles(flag, traces):
    if flag:
        for trace in traces:
            trace.draw(screen)
            trace.update()


def draw_traces_obstacles(flag, traces):
    if flag:
        for w_trace in traces:
            w_trace.draw_trace(screen)


def game_cycle(l_id):
    sound('Music/1679007940657971.ogg', False)
    sound(select_one_with_aspect('Levels', 'id', l_id, 'music_level')[0], True)
    all_circles.add(red_circle, blue_circle)
    all_circles.add(red_circle, blue_circle)
    game = True
    walls_group = create_obst_group(l_id)
    traces_wall = []
    bank_amount = get_bank(l_id)

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
        draw_pause()
        print_text(screen, f'Dodged: {get_dodged(walls_group)}', 10, 10, 20)
        print_text(screen, f'Банк: {bank_amount} монет', 10, 30, 20)
        print_level_number(screen, l_id)

        draw_gray_circle()
        draw_traces_for_circles(select_table('settings', 'effects')[0][0], circle_movement.traces)
        draw_traces_obstacles(select_table('settings', 'effects')[0][0], traces_wall)
        walls_group.update()
        loc_walls_group.draw(screen)
        all_circles.draw(screen)

        pygame.display.update()
        fps_clock.tick(FPS)
        if check_level_complited(walls_group):
            next_level(l_id)


def next_level(level_id):
    game = True

    coins_amount = get_bank(level_id)
    nullify_coins(level_id)
    pay_coins(coins_amount)

    coin_group = pygame.sprite.Group()
    coin = AnimatedSprite(load_image(COINS_SHEET), 10, 1, 437, 338)
    coin.add(coin_group)

    counter = 0

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                quit()
        press_key(red_circle, blue_circle)
        coin_group.update()
        screen.fill(BLACK_COLOR)

        print_text(screen, LEVEL_COMPLITED, 150, 270, 40)
        print_text(screen, f'Вы получаете: {coins_amount} монет', 110, 350, 40)
        draw_gray_circle()
        coin_group.draw(screen)
        draw_traces_for_circles(select_table('settings', 'effects')[0][0], circle_movement.traces)
        all_circles.draw(screen)

        if counter >= 250:
            screen.fill(BLACK_COLOR)
        if counter == 300:
            game_cycle(ALL_LEVELS[ALL_LEVELS.index(level_id) + 1])

        pygame.display.update()
        fps_clock.tick(FPS)
        counter += 1

if __name__ == '__main__':
    start_game(SIZE)
