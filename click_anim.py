import pygame
from parametres import *
from general_functions import *

click_counter = 0
draw_click = False


def draw_click(scr):
    global click_counter
    global draw_click
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[GET_ZERO_VALUES] or click[GET_FIRST_VALUES]:
        draw_click = True

    if draw_click:
        draw_x = mouse[GET_ZERO_VALUES] - CLICK_SIZE[click_counter] // 2
        draw_y = mouse[GET_FIRST_VALUES] - CLICK_SIZE[click_counter] // 2
        scr.blit(CLICK_IMG[click_counter], (draw_x, draw_y))
        click_counter += 1
        if click_counter == 10:
            click_counter = 0
            draw_click = False


CLICK_IMG = [load_image('click_pics/Light0.png'), load_image('click_pics/Light1.png'),
             load_image('click_pics/Light2.png'), load_image('click_pics/Light3.png'),
             load_image('click_pics/Light4.png'), load_image('click_pics/Light5.png'),
             load_image('click_pics/Light6.png'), load_image('click_pics/Light7.png'),
             load_image('click_pics/Light8.png'), load_image('click_pics/Light9.png'),
             load_image('click_pics/Light10.png')]
