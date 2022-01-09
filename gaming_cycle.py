import circle_movement
from Button import Button
from walls import *
import menu_for_all
from mouse_cursor import Mouse
from load_music import *
from cut_sheet import *
import gif
import random
from click_anim import draw_click
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
currentFrame = 0
gifFrameList = gif.loadGIF(f"{PATH_GIF}{1}{GIF}")
paused = True

id_colors = select_one_with_aspect(LOCKERS_DB, AVAILABILITY, AVAILABILITY_TRUE, ID)[GET_ZERO_VALUES]
if id_colors == ID_ITEM_FIRST:
    circle1 = circle_movement.Circles(
        RED_CIRCLE_IMG, RED_CIRCLE_START_ANGLE, RED_CIRCLE_START_X, RED_CIRCLE_START_Y, RED)
    circle2 = circle_movement.Circles(
        BLUE_CIRCLE_IMG, BLUE_CIRCLE_START_ANGLE, BLUE_CIRCLE_START_X, BLUE_CIRCLE_START_Y, BLUE)
else:
    circle1 = circle_movement.Circles(
        GOLUB_CIRCLE_IMG, RED_CIRCLE_START_ANGLE, RED_CIRCLE_START_X, RED_CIRCLE_START_Y, GOL)
    circle2 = circle_movement.Circles(
        IZUMRUD_CIRCLE_IMG, BLUE_CIRCLE_START_ANGLE, BLUE_CIRCLE_START_X, BLUE_CIRCLE_START_Y, IZUMRUD)


def off_pause():
    global paused
    paused = False


def draw_pause():
    btn_pause = Button(screen, BTN_PAUSE_RECT, BTN_PAUSE_RECT, inactive_col=None)
    btn_pause.draw(x=560, y=0, message=PAUSE_BTN_TEXT, action=pause, font_size=FONT_THIRTY_SIZE)


def draw_gray_circle():
    pygame.draw.circle(screen, DEEP_GRAY, GRAY_CIRCLE_POSITION,
                       GRAY_CIRCLE_RADIUS, GRAY_CIRCLE_WIDTH)


def game_over(walls_group, red, blue, speed=None):
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
                quit_game()
        if max(list(map(lambda x: x.rect.y, walls_group))) < MAX_WALLS_Y:
            game = False
        for w_trace in traces_wall:
            w_trace.draw_trace(screen)
        for i in walls_group:
            i.speed_y -= SPEED_CHANGING
        changing_speed(red, blue, speed, True, RED_CIRCLE_START_ANGLE, BLUE_CIRCLE_START_ANGLE)
        gif_background(screen)
        draw_pause()
        draw_gray_circle()
        walls_group.update()
        all_circles.draw(screen)
        draw_traces_for_circles(select_table(SETTINGS, EFFECTS)[0][0], circle_movement.traces)
        loc_walls_group.draw(screen)
        draw_click(screen)
        pygame.display.update()
        fps_clock.tick(FPS_SIXTY)


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
    return menu_for_all.Menu(SIZE).main_menu().event_loop()


def race_score_menu(name, score):
    return menu_for_all.Menu(SIZE).race_score_menu(name, score).event_loop()


def pause():
    global paused
    btn_resume_game = Button(screen, BTN_RESUME_X, BTN_RESUME_Y)
    btn_leave_hub = Button(screen, BTN_LEAVE_HUB_X, BTN_LEAVE_HUB_Y)
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        screen.fill(BLACK_COLOR)
        print_text(screen, message=PAUSE_ACTIONS, x=40, y=300, font_type=FONT_DROID)
        keys = pygame.key.get_pressed()
        btn_resume_game.draw(x=325, y=290, message=BTN_CONTINUE_TEXT, action=off_pause, font_size=FONT_THIRTY_SIZE)
        btn_leave_hub.draw(x=320, y=350, message=BTN_LEAVE_TEXT, action=call_menu, font_size=FONT_THIRTY_SIZE)

        if keys[pygame.K_RETURN]:
            paused = False
        draw_click(screen)
        pygame.display.update()
        fps_clock.tick(FPS_FIFTEEN)


def get_walls(lev_id):
    return [
        get_obstacles(lev_id, TWIST_OBSTACLES),
        get_obstacles(lev_id, LF_DOWN_OBSTACLES),
        get_obstacles(lev_id, SIDE_OBSTACLES)
    ]


def add_walls_to_group(group, twist_walls, lf_walls, side_walls):
    for wall in twist_walls:
        wall_sprite = TwistObstacle(*wall)
        wall_sprite.add(group)

    for wall in lf_walls:
        wall_sprite = LfDownObstacle(*wall)
        wall_sprite.add(group)

    for wall in side_walls:
        wall_sprite = SlideSideObstacle(*wall)
        wall_sprite.add(group)


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
        for i in range(len(res) - NUM_TO_DEL_TRACE, -NUM_TO_DEL_TRACE, -NUM_TO_DEL_TRACE):
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
    global currentFrame
    rect = gifFrameList[currentFrame].get_rect()
    scr.blit(gifFrameList[currentFrame], rect)
    currentFrame = (currentFrame + CHANGE_FRAME_GIF) % len(gifFrameList)


def update_gif():
    global gifFrameList
    num = random.randint(MIN_RANDOM_GIF, MAX_RANDOM_GIF)
    gifFrameList = gif.loadGIF(f"gifs/top_gif_{num}.gif")


def infinity_cycle(player_name, speed=1, score=0, lives=INFINITY_LEVEL_LIVES, level_id=INFINITY_LEVEL_ID):
    global currentFrame
    global counter_quotes
    if counter_quotes % 10 == 0:
        sound_effects(f'{SAME_LINK_FOR_QUOTES}{level_id}{FORMAT_OGG}', select_table(SETTINGS, VOICE)[0][0])
    counter_quotes += 1
    sound(MENU_MUSIC, select_table(SETTINGS, MUSIC)[0][0])
    sound(select_one_with_aspect(LEVELS, ID, level_id, MUSIC_LEVEL)[0],
          select_table(SETTINGS, MUSIC)[0][0])
    all_circles.add(circle1, circle2)
    game = True
    walls = get_walls(level_id)
    walls_group = pygame.sprite.Group()
    add_walls_to_group(walls_group, *walls)
    traces_wall = []
    bank_amount = get_bank(level_id)
    dodged_removed = score

    while game:
        loc_walls_group = get_loc_walls_gr(walls_group)
        traces_wall = get_traces_arr(loc_walls_group, traces_wall)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                quit_game()
        gif_background(screen)
        press_key(circle1, circle2, speed=SPEED_MOVEMENT_TRUE)
        dodged = dodged_removed + get_dodged(walls_group)

        if any([circle1.check_collision(screen, walls_group),
                circle2.check_collision(screen, walls_group)]):
            sound_effects(SOUND_COLLUSION,
                          select_table(SETTINGS, SOUND_EFFECTS)[0][0])
            if lives <= FIRST_ITEM:
                save_infinity_score(player_name, dodged)
                return race_score_menu(player_name, dodged)
            else:
                game_over(walls_group, circle1, circle2, SPEED_MOVEMENT_TRUE)
                return infinity_cycle(player_name, speed, dodged, lives - 1)

        draw_pause()
        print_text(screen, f'{DODGED_MESS} {dodged}', x=10, y=10, font_size=FONT_TWENTY_SIZE)
        print_text(screen, f'{BANK_MESSAGE} {bank_amount} {COIN_MESSAGE}', x=10, y=30, font_size=FONT_TWENTY_SIZE)
        print_text(screen, f'{LIVES_TEXT} {lives}', x=490, y=10, font_size=FONT_TWENTY_SIZE)
        print_text(screen, f'{SPEED_TEXT} {int(100 * speed)}%', x=490, y=25, font_size=FONT_TWENTY_SIZE)

        draw_gray_circle()
        draw_traces_for_circles(select_table(SETTINGS, EFFECTS)[GET_ZERO_VALUES][GET_ZERO_VALUES],
                                circle_movement.traces)
        draw_traces_obstacles(select_table(SETTINGS, EFFECTS)[GET_ZERO_VALUES][GET_ZERO_VALUES], traces_wall)
        walls_group.update()
        loc_walls_group.draw(screen)
        all_circles.draw(screen)
        draw_click(screen)
        pygame.display.update()
        fps_clock.tick(FPS_SIXTY)
        dodged_removed += remove_passed_sprites(walls_group)
        if len(walls_group) <= FIRST_ITEM:
            speed *= INF_SPEED_MUL
            add_walls_to_group(walls_group, *increase_speed(walls, speed))


def game_cycle(l_id):
    global currentFrame
    global counter_quotes
    if counter_quotes % PLAY_EVERY_TEN_TIMES == CHECK_PLAY_QUOTE:
        sound_effects(f'{SAME_LINK_FOR_QUOTES}{l_id}{FORMAT_OGG}', select_table(SETTINGS, VOICE)[0][0])
    counter_quotes += FIRST_ITEM
    sound(MENU_MUSIC, select_table(SETTINGS, MUSIC)[GET_ZERO_VALUES][GET_ZERO_VALUES])
    sound(select_one_with_aspect(LEVELS, ID, l_id, MUSIC_LEVEL)[GET_ZERO_VALUES],
          select_table(SETTINGS, MUSIC)[GET_ZERO_VALUES][GET_ZERO_VALUES])
    all_circles.add(circle1, circle2)
    all_circles.add(circle1, circle2)
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
                quit_game()
        gif_background(screen)
        press_key(circle1, circle2, speed=SPEED_MOVEMENT_TRUE)

        if any([circle1.check_collision(screen, walls_group),
                circle2.check_collision(screen, walls_group)]):
            sound_effects(SOUND_COLLUSION,
                          select_table(SETTINGS, SOUND_EFFECTS)[GET_ZERO_VALUES][GET_ZERO_VALUES])
            game_over(walls_group, circle1, circle2, speed=SPEED_MOVEMENT_TRUE)
            return game_cycle(l_id)

        draw_pause()
        print_text(screen, f'{DODGED_MESS} {get_dodged(walls_group)}', x=10, y=10, font_size=FONT_TWENTY_SIZE)
        print_text(screen, f'{BANK_MESSAGE} {bank_amount} {COIN_MESSAGE}', x=10, y=30, font_size=FONT_TWENTY_SIZE)
        print_level_number(screen, l_id)
        draw_gray_circle()
        draw_traces_for_circles(select_table(SETTINGS, EFFECTS)[GET_ZERO_VALUES][GET_ZERO_VALUES],
                                circle_movement.traces)
        draw_traces_obstacles(select_table(SETTINGS, EFFECTS)[GET_ZERO_VALUES][GET_ZERO_VALUES], traces_wall)
        walls_group.update()
        loc_walls_group.draw(screen)
        all_circles.draw(screen)
        draw_click(screen)
        pygame.display.update()
        fps_clock.tick(FPS_SIXTY)
        if check_level_complited(walls_group):
            counter_quotes = ZEROING_QUOTES
            currentFrame = ZEROING_FRAMES
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
                quit_game()
        gif_background(screen)
        press_key(circle1, circle2, speed=SPEED_MOVEMENT_TRUE)
        coin_group.update()

        print_text(screen, LEVEL_COMPLITED, x=150, y=270, font_size=FONT_FORTY_SIZE)
        print_text(screen, f'{BANK_MESSAGE} {coins_amount} {COIN_MESSAGE}', x=110, y=350,
                   font_size=FONT_FORTY_SIZE)
        draw_gray_circle()
        coin_group.draw(screen)
        draw_traces_for_circles(select_table(SETTINGS, EFFECTS)[0][0], circle_movement.traces)
        all_circles.draw(screen)

        if counter >= 250:
            gif_background(screen)
        if counter == 300:
            if level_id == MAX_LEVEL:
                call_menu()
            game_cycle(ALL_LEVELS[ALL_LEVELS.index(level_id) + INCREASE_LEVELS])
        draw_click(screen)
        pygame.display.update()
        fps_clock.tick(FPS_SIXTY)
        counter += INCREASE_LEVELS
