import pygame
from parametres import *
import circle_movement
from general_functions import *
from Button import Button
from walls import *
import menu_for_all
from mouse_cursor import Mouse
from load_music import *
from cut_sheet import *
import main
import gif

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

icon = load_image(ICON_IMG)
pygame.display.set_icon(icon)
all_circles = pygame.sprite.Group()
all_obstacles = pygame.sprite.Group()
fps_clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
mouse = Mouse()
all_sprites.add(mouse)
scores = 0
counter_quotes = 0
gifFrameList = gif.loadGIF(f"gifs/top_gif_{1}.gif")
paused = True

red_circle = circle_movement.Circles(
    RED_CIRCLE_IMG, RED_CIRCLE_START_ANGLE, RED_CIRCLE_START_X, RED_CIRCLE_START_Y, RED)
blue_circle = circle_movement.Circles(
    BLUE_CIRCLE_IMG, BLUE_CIRCLE_START_ANGLE, BLUE_CIRCLE_START_X, BLUE_CIRCLE_START_Y, BLUE)


def off_pause():
    global paused
    paused = False


def draw_pause():
    btn_pause = Button(screen, 30, 30, inactive_col=None)
    btn_pause.draw(560, 0, PAUSE_BTN_TEXT, pause, 30)


def draw_gray_circle():
    pygame.draw.circle(screen, DEEP_GRAY_COLOR_1, GRAY_CIRCLE_POSITION,
                       GRAY_CIRCLE_RADIUS, GRAY_CIRCLE_WIDTH)


def game_over(walls_group, l_id, red, blue, speed=None):
    game = True
    traces_wall = []
    sound_effects(SOUND_RESTART,
                  select_table(SETTINGS, SOUND_EFFECTS)[0][0])
    while game:
        loc_walls_group = get_loc_walls_gr(walls_group)
        traces_wall = get_traces_arr(loc_walls_group, traces_wall)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                quit()
        if max(list(map(lambda x: x.rect.y, walls_group))) < -350:
            game = False
        for w_trace in traces_wall:
            w_trace.draw_trace(screen)
        for i in walls_group:
            i.speed_y -= 1.5
        changing_speed(red, blue, speed, True, RED_CIRCLE_START_ANGLE, BLUE_CIRCLE_START_ANGLE)
        gif_background(screen)
        draw_pause()
        draw_gray_circle()
        walls_group.update()
        all_circles.draw(screen)
        draw_traces_for_circles(select_table(SETTINGS, EFFECTS)[0][0], circle_movement.traces)
        loc_walls_group.draw(screen)

        pygame.display.update()
        fps_clock.tick(FPS_SIXTY)
    game_cycle(l_id)


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


def call_menu():
    return menu_for_all.Menu(SIZE)


def pause():
    global paused
    btn_resume_game = Button(screen, BTN_RESUME_X, BTN_RESUME_Y)
    btn_leave_hub = Button(screen, BTN_LEAVE_HUB_X, BTN_LEAVE_HUB_Y)
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.fill(BLACK_COLOR)
        print_text(screen, message=PAUSE_ACTIONS, x=40, y=300, font_type=FONT_DROID)
        keys = pygame.key.get_pressed()
        btn_resume_game.draw(325, 290, BTN_CONTINUE_TEXT, off_pause, FONT_THIRTY_SIZE)
        btn_leave_hub.draw(320, 350, BTN_LEAVE_TEXT, call_menu, FONT_THIRTY_SIZE)

        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        fps_clock.tick(FPS_FIFTEEN)


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


def press_key(red, blue, speed):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pause()
    if keys[pygame.K_RIGHT]:
        changing_speed(red, blue, speed, True)
    if keys[pygame.K_LEFT]:
        changing_speed(red, blue, -speed, False)


def draw_traces_for_circles(flag, traces):
    if flag:
        for trace in traces:
            trace.draw(screen)
            trace.update()


def draw_traces_obstacles(flag, traces):
    if flag:
        for w_trace in traces:
            w_trace.draw_trace(screen)


def gif_background(scr):
    rect = gifFrameList[gif.currentFrame].get_rect()
    scr.blit(gifFrameList[gif.currentFrame], rect)
    gif.currentFrame = (gif.currentFrame + 1) % len(gifFrameList)


def update_gif():
    global gifFrameList
    num = random.randint(1, 5)
    gifFrameList = gif.loadGIF(f"gifs/top_gif_{num}.gif")


def game_cycle(l_id):
    global counter_quotes
    if counter_quotes % 10 == 0:
        sound_effects(f'{SAME_LINK_FOR_QUOTES}{l_id}{FORMAT_OGG}', select_table(SETTINGS, VOICE)[0][0])
    counter_quotes += 1
    sound(MENU_MUSIC, select_table(SETTINGS, MUSIC)[0][0])
    sound(select_one_with_aspect(LEVELS, ID, l_id, MUSIC_LEVEL)[0],
          select_table(SETTINGS, MUSIC)[0][0])
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
        gif_background(screen)
        press_key(red_circle, blue_circle, speed=SPEED_MOVEMENT_TRUE)

        if any([red_circle.check_collision(screen, walls_group),
                blue_circle.check_collision(screen, walls_group)]):
            sound_effects(SOUND_COLLUSION,
                          select_table(SETTINGS, SOUND_EFFECTS)[0][0])
            return game_over(walls_group, l_id, red_circle, blue_circle, speed=SPEED_MOVEMENT_TRUE)

        draw_pause()
        print_text(screen, f'{DODGED_MESS} {get_dodged(walls_group)}', 10, 10, FONT_TWENTY_SIZE)
        print_text(screen, f'{BANK_MESSAGE} {bank_amount} {COIN_MESSAGE}', 10, 30, FONT_TWENTY_SIZE)
        print_level_number(screen, l_id)

        draw_gray_circle()
        draw_traces_for_circles(select_table(SETTINGS, EFFECTS)[0][0], circle_movement.traces)
        draw_traces_obstacles(select_table(SETTINGS, EFFECTS)[0][0], traces_wall)
        walls_group.update()
        loc_walls_group.draw(screen)
        all_circles.draw(screen)

        pygame.display.update()
        fps_clock.tick(FPS_SIXTY)
        if check_level_complited(walls_group):
            counter_quotes = 0
            gif.currentFrame = 0
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
    update_gif()
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                quit()
        gif_background(screen)
        draw_pause()
        press_key(red_circle, blue_circle, speed=SPEED_MOVEMENT_TRUE)
        coin_group.update()

        print_text(screen, LEVEL_COMPLITED, 150, 270, FONT_FORTY_SIZE)
        print_text(screen, f'{BANK_MESSAGE} {coins_amount} {COIN_MESSAGE}', 110, 350,
                   FONT_FORTY_SIZE)
        draw_gray_circle()
        coin_group.draw(screen)
        draw_traces_for_circles(select_table(SETTINGS, EFFECTS)[0][0], circle_movement.traces)
        all_circles.draw(screen)

        if counter >= 250:
            gif_background(screen)
        if counter == 300:
            if level_id == 66:
                call_menu()
            game_cycle(ALL_LEVELS[ALL_LEVELS.index(level_id) + 1])

        pygame.display.update()
        fps_clock.tick(FPS_SIXTY)
        counter += 1
