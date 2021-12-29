import os
import sys
import pygame
import random
from parametres import *
from general_functions import *

pygame.init()


# 1 - (НЕ РЕАЛИЗОВАНО) - выезд платформы по вертикали
# 2 - SIDE - выезд платформы по горизонтали
# 3 - (НЕ РЕАЛИЗОВАНО) - постоянные движения по горизонтали
# 4 - TWIST - кручение платформы


class LfDownObstacle(pygame.sprite.Sprite):
    def __init__(self, *obst_params):
        super().__init__(all_sprites)
        self.x_move, self.y_move = BASE_X_MOVE, BASE_Y_MOVE
        self.image = load_image(obst_params[INX_IMG_NAME])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y, self.angle = \
            obst_params[INX_X_POS], obst_params[INX_Y_POS], obst_params[INX_STATIC_ANGLE]
        self.speed_x, self.speed_y = obst_params[INX_X_SPEED], obst_params[INX_Y_SPEED]
        self.y_start_down, self.y_end_down, self.step_speed_down = [UNDEFINED] * 3
        self.left_board_lf, self.right_board_lf, self.step_speed_lf = [UNDEFINED] * 3
        self.frames = ZERO_FRAMES

    def load_down_move_args(self):
        self.y_start_down = obst_params[INX_Y_START_DOWN]
        self.y_end_down = obst_params[INX_Y_END_DOWN]
        self.step_speed_down = obst_params[INX_STEP_SPEED_DOWN]

    def load_lf_move_args(self):
        self.left_board_lf = obst_params[INX_LEFT_BOARD_LF]
        self.right_board_lf = obst_params[INX_RIGHT_BOARD_LF]
        self.step_speed_lf = obst_params[INX_STEP_SPEED_LF]

    def update(self):
        self.update_move_x()
        self.update_move_y()
        self.rect = self.rect.move(self.x_move, self.y_move)

    def update_move_x(self):
        if self.left_board_lf < self.rect.x < self.right_board_lf:
            if self.frames == SIXTY_FRAMES:
                self.x_move = self.speed_x + self.step_speed_lf
            if self.frames == ZERO_FRAMES:
                self.x_move = self.speed_x - self.step_speed_lf
        else:
            if self.left_board_lf == self.rect.x:
                self.frames += ONE_FRAME
            else:
                self.frames -= ONE_FRAME

    def update_move_y(self):
        if self.y_end_down <= self.rect.y <= self.y_end_down:
            self.y_move = self.step_speed_down + self.speed_y
        else:
            self.y_move = self.speed_y


class SlideSideObstacle(pygame.sprite.Sprite):
    def __init__(self, *obst_params):
        super().__init__(all_sprites)
        self.x_move, self.y_move = BASE_X_MOVE, BASE_Y_MOVE
        self.image = load_image(obst_params[INX_IMG_NAME])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y, self.angle = \
            obst_params[INX_X_POS], obst_params[INX_Y_POS], obst_params[INX_ANGLE]
        self.speed_x, self.speed_y = obst_params[INX_X_SPEED], obst_params[INX_Y_SPEED]
        self.y_start_side, self.y_end_side, self.step_speed_side = \
            obst_params[INX_Y_START_SIDE], obst_params[INX_Y_END_SIDE], obst_params[INX_STEP_SPEED_SIDE]

    def update(self):
        if self.y_start_side <= self.rect.y <= self.y_end_side:
            self.x_move = self.step_speed_side + self.speed_x
            self.y_move = self.speed_x
        else:
            self.y_move = self.speed_x
            self.x_move = self.speed_x

        self.rect = self.rect.move(self.x_move, self.y_move)


class TwistObstacle(pygame.sprite.Sprite):
    def __init__(self, *obst_params):
        super().__init__(all_sprites)
        self.image = load_image(obst_params[INX_IMG_NAME])
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = obst_params[INX_X_POS], obst_params[INX_Y_POS]
        self.speed_x, self.speed_y = obst_params[INX_X_SPEED], obst_params[INX_Y_SPEED]
        self.rotated_surface, self.rotated_rect = UNDEFINED, UNDEFINED
        self.step_angle, self.start_angle = \
            obst_params[INX_STEP_ANG_TWIST], obst_params[INX_BASE_ANG_TWIST]

    def update(self):
        if self.start_angle > 0:
            self.start_angle -= self.step_angle
        else:
            self.start_angle = 0
            self.angle += self.infin_twist_angle
        self.rect = self.rect.move(self.speed_x, self.speed_y)
        self.rotated_surface = pygame.transform.rotate(self.image, self.angle)
        self.rotated_rect = self.rotated_surface.get_rect(center=(self.rect.x, self.rect.y))

    def get_surf_rect(self):
        return self.rotated_surface, self.rotated_rect


class ShowObstacle(pygame.sprite.Sprite):
    def __init__(self, img, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = rect
        self.mask = pygame.mask.from_surface(self.image)

# def delete_wall(walls_list):
#     for enemy in walls_list:
#         if enemy.rect.y > 900:
#             walls_list.remove(enemy)
#
#
# def create_walls(array_walls1):
#     for i in range(len(array_walls1)):
#         array_walls1[i][INX_Y_POS] = array_walls1[i][INX_Y_POS] + array_walls1[i][INX_Y_SPEED]
#         array_walls1[i][INX_X_POS] = array_walls1[i][INX_X_POS] + array_walls1[i][INX_X_SPEED]
#         if array_walls1[i][INX_Y_POS] >= 0 and array_walls1[i][INX_INVIZ]:
#             array_walls1[i][INX_INVIZ] = False
#             Wall1(array_walls1[i])
#
#
# size = width, height = WIDTH, HIGHT
# screen = pygame.display.set_mode(size)
#
# clock = pygame.time.Clock()
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     create_walls(array_walls1)
#     count += 1
#     print(count, len(all_sprites))
#
#     delete_wall(all_sprites)
#
#     all_sprites.update()
#     screen.fill('black')
#     all_sprites.draw(screen)
#     pygame.display.flip()
#
#     clock.tick(FPS)
# pygame.quit()
