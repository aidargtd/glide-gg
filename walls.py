import os
import sys
import pygame
import random
from parametres import *
from general_functions import *

pygame.init()


# 1 - LF_DOWN - выезд платформы по вертикали
# 2 - SIDE - выезд платформы по горизонтали
# 3 - LF_DOWN - постоянные движения по горизонтали
# 4 - TWIST - кручение платформы

class LfDownObstacle(pygame.sprite.Sprite):
    def __init__(self, *args):
        pygame.sprite.Sprite.__init__(self)
        self.x_move, self.y_move = BASE_X_MOVE, BASE_Y_MOVE
        # 1. Загрузка базовой информации о препятствии
        self.image, self.rect, self.mask, self.speed_x, self.speed_y = [UNDEFINED] * 5
        self.load_base_obst_args(args)
        # 2. Загрузка информации о движении вниз
        self.y_start_down, self.y_end_down, self.step_speed_down = [UNDEFINED] * 3
        self.load_down_move_args(args)
        # 1. Загрузка информации о движении влево-вправо
        self.left_board_lf, self.right_board_lf, self.step_speed_lf, self.frames = [UNDEFINED] * 4
        self.load_lf_move_args(args)

    def load_base_obst_args(self, move_inf):
        self.image = load_image(move_inf[INX_IMG_NAME])
        self.image = pygame.transform.rotate(self.image, move_inf[INX_STATIC_ANGLE])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = move_inf[INX_X_POS]
        self.rect.y = move_inf[INX_Y_POS]
        self.speed_x = move_inf[INX_X_SPEED]
        self.speed_y = move_inf[INX_Y_SPEED]

    def load_down_move_args(self, move_inf):
        self.y_start_down = move_inf[INX_Y_START_DOWN]
        self.y_end_down = move_inf[INX_Y_END_DOWN]
        self.step_speed_down = move_inf[INX_STEP_SPEED_DOWN]

    def load_lf_move_args(self, move_inf):
        self.left_board_lf = move_inf[INX_LEFT_BOARD_LF]
        self.right_board_lf = move_inf[INX_RIGHT_BOARD_LF]
        self.step_speed_lf = move_inf[INX_STEP_SPEED_LF]
        self.frames = ZERO_FRAMES

    def update(self):
        # print(self.rect.x, self.rect.y, self.frames)
        self.update_move_x()
        self.update_move_y()
        self.rect = self.rect.move(self.x_move, self.y_move)

    # Левое положение: от 0 -> 10
    # Правое положение: от 10 -> 0
    def update_move_x(self):
        self.x_move = self.speed_x
        if self.step_speed_lf != 0:
            if self.left_board_lf < self.rect.x < self.right_board_lf:
                if self.frames == LIMIT_FRAME:
                    self.x_move = self.speed_x + self.step_speed_lf
                if self.frames == ZERO_FRAMES:
                    self.x_move = self.speed_x - self.step_speed_lf
            elif self.left_board_lf >= self.rect.x:
                if self.frames == LIMIT_FRAME:
                    self.x_move = self.step_speed_lf + self.speed_x
                else:
                    self.frames += STEP_FRAME
            elif self.right_board_lf <= self.rect.x:
                if self.frames == ZERO_FRAMES:
                    self.x_move = - self.step_speed_lf + self.speed_x
                else:
                    self.frames -= STEP_FRAME

    def update_move_y(self):
        if self.y_start_down <= self.rect.y <= self.y_end_down:
            self.y_move = self.step_speed_down + self.speed_y
        else:
            self.y_move = self.speed_y


class SlideSideObstacle(pygame.sprite.Sprite):
    def __init__(self, *args):
        pygame.sprite.Sprite.__init__(self)
        self.x_move, self.y_move = BASE_X_MOVE, BASE_Y_MOVE
        # 1. Загрузка базовой информации о препятствии
        self.image, self.rect, self.mask, self.speed_x, self.speed_y = [UNDEFINED] * 5
        self.load_base_obst_args(args)
        # 2. Загрузка информации о выезде вбок
        self.y_start_side, self.y_end_side, self.step_speed_side = [UNDEFINED] * 3
        self.load_side_move_args(args)

    def load_base_obst_args(self, move_inf):
        self.image = load_image(move_inf[INX_IMG_NAME])
        self.image = pygame.transform.rotate(self.image, move_inf[INX_STATIC_ANGLE])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = move_inf[INX_X_POS]
        self.rect.y = move_inf[INX_Y_POS]
        self.speed_x = move_inf[INX_X_SPEED]
        self.speed_y = move_inf[INX_Y_SPEED]

    def load_side_move_args(self, move_inf):
        self.y_start_side = move_inf[INX_Y_START_SIDE]
        self.y_end_side = move_inf[INX_Y_END_SIDE]
        self.step_speed_side = move_inf[INX_STEP_SPEED_SIDE]

    def update(self):
        if self.y_start_side <= self.rect.y <= self.y_end_side:
            self.x_move = self.step_speed_side + self.speed_x
        else:
            self.x_move = self.speed_x
        self.y_move = self.speed_y

        self.rect = self.rect.move(self.x_move, self.y_move)

    def get_surf_rect(self):
        return self.image, self.rect


class TwistObstacle(pygame.sprite.Sprite):
    def __init__(self, *args):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.deep_image_copy = load_image(args[INX_IMG_NAME])
        self.rect = self.deep_rect_copy = self.image.get_rect()
        self.rect.x, self.rect.y = args[INX_X_POS], args[INX_Y_POS]
        self.deep_rect_copy.x, self.deep_rect_copy.y = args[INX_X_POS], args[INX_Y_POS]
        self.speed_x, self.speed_y = args[INX_X_SPEED], args[INX_Y_SPEED]
        self.step_angle, self.start_angle = \
            args[INX_STEP_ANG_TWIST], args[INX_BASE_ANG_TWIST]
        self.angle = BASE_STATIC_ANGLE
        self.counter = 0

    def update(self):
        if -200 <= self.deep_rect_copy.y <= 900:
            if self.start_angle > 0:
                if self.counter % 15 == 0:
                    self.start_angle -= self.step_angle
            else:
                self.start_angle = 0
            self.counter += 1

            self.angle += self.start_angle

        self.deep_rect_copy = self.deep_rect_copy.move(self.speed_x, self.speed_y)
        if -200 <= self.deep_rect_copy.y <= 900:
            self.image = pygame.transform.rotate(self.deep_image_copy, self.angle)
            self.rect = self.image.get_rect(center=(self.deep_rect_copy.x, self.deep_rect_copy.y))

    # def get_surf_rect(self):
    #     return self.rotated_surface, self.rotated_rect


class ShowObstacle(pygame.sprite.Sprite):
    def __init__(self, img, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = rect
        self.mask = pygame.mask.from_surface(self.image)
