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
        self.image, self.deep_image, self.rect, self.mask = [UNDEFINED] * 4
        self.speed_x, self.speed_y, self.static_angle = [UNDEFINED] * 3
        self.load_base_obst_args(args)
        # 2. Загрузка информации о движении вниз
        self.y_start_down, self.y_end_down, self.step_speed_down = [UNDEFINED] * 3
        self.load_down_move_args(args)
        # 1. Загрузка информации о движении влево-вправо
        self.left_board_lf, self.right_board_lf, self.step_speed_lf, self.frames = [UNDEFINED] * 4
        self.load_lf_move_args(args)

    def load_base_obst_args(self, move_inf):
        self.image = self.deep_image = load_image(move_inf[INX_IMG_NAME])
        self.static_angle = move_inf[INX_STATIC_ANGLE]
        self.image = pygame.transform.rotate(self.image, self.static_angle)
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
        self.update_move_x()
        self.update_move_y()
        self.rect = self.rect.move(self.x_move, self.y_move)

    def get_trace_inf(self):
        rect = self.deep_image.get_rect()
        return [self.rect.x, self.rect.y, rect.width, rect.height, self.static_angle]

    def update_move_x(self):
        self.x_move = self.speed_x
        if self.step_speed_lf != 0 and check_sane_y_cord(self.rect.y):
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
        if self.y_start_down <= self.rect.y <= self.y_end_down and \
                check_sane_y_cord(self.rect.y):
            self.y_move = self.step_speed_down + self.speed_y
        else:
            self.y_move = self.speed_y

    def get_angle(self):
        return self.static_angle


class SlideSideObstacle(pygame.sprite.Sprite):
    def __init__(self, *args):
        pygame.sprite.Sprite.__init__(self)
        self.x_move, self.y_move = BASE_X_MOVE, BASE_Y_MOVE
        # 1. Загрузка базовой информации о препятствии
        self.image, self.deep_image, self.rect, self.mask = [UNDEFINED] * 4
        self.speed_x, self.speed_y, self.static_angle = [UNDEFINED] * 3
        self.load_base_obst_args(args)
        # 2. Загрузка информации о выезде вбок
        self.y_start_side, self.y_end_side, self.step_speed_side = [UNDEFINED] * 3
        self.load_side_move_args(args)

    def load_base_obst_args(self, move_inf):
        self.image = self.deep_image = load_image(move_inf[INX_IMG_NAME])
        self.static_angle = move_inf[INX_STATIC_ANGLE]
        self.image = pygame.transform.rotate(self.image, self.static_angle)
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
        if self.y_start_side <= self.rect.y <= self.y_end_side and check_sane_y_cord(self.rect.y):
            self.x_move = self.step_speed_side + self.speed_x
        else:
            self.x_move = self.speed_x
        self.y_move = self.speed_y

        self.rect = self.rect.move(self.x_move, self.y_move)

    def get_trace_inf(self):
        rect = self.deep_image.get_rect()
        return [self.rect.x, self.rect.y, rect.width, rect.height, self.static_angle]


class TwistObstacle(pygame.sprite.Sprite):
    def __init__(self, *args):
        pygame.sprite.Sprite.__init__(self)

        self.x_move, self.y_move = BASE_X_MOVE, BASE_Y_MOVE
        # 1. Загрузка базовой информации о препятствии
        self.image, self.deep_image_copy, self.rect, self.deep_rect_copy = [UNDEFINED] * 4
        self.speed_x, self.speed_y, self.static_angle, self.mask = [UNDEFINED] * 4
        self.load_base_obst_args(args)
        # 2. Загрузка информации препятствия о вращении
        self.step_angle, self.start_angle = args[INX_STEP_ANG_TWIST], args[INX_BASE_ANG_TWIST]
        self.static_angle = BASE_STATIC_ANGLE
        self.mask = pygame.mask.from_surface(self.image)
        self.counter = 0

    def load_base_obst_args(self, args):
        self.image = self.deep_image_copy = load_image(args[INX_IMG_NAME])
        self.rect = self.deep_rect_copy = self.image.get_rect()
        self.rect.x, self.rect.y = args[INX_X_POS], args[INX_Y_POS]
        self.deep_rect_copy.x, self.deep_rect_copy.y = args[INX_X_POS], args[INX_Y_POS]
        self.speed_x, self.speed_y = args[INX_X_SPEED], args[INX_Y_SPEED]

    def update(self):
        if check_sane_y_cord(self.deep_rect_copy.y):
            if self.start_angle > 0:
                if self.counter % 15 == 0:
                    self.start_angle -= self.step_angle
            else:
                self.start_angle = 0
            self.counter += 1

            self.static_angle += self.start_angle

            self.image = pygame.transform.rotate(self.deep_image_copy, self.static_angle)
            self.rect = self.image.get_rect(center=(self.deep_rect_copy.x, self.deep_rect_copy.y))
        self.mask = pygame.mask.from_surface(self.image)
        self.deep_rect_copy = self.deep_rect_copy.move(self.speed_x, self.speed_y)

    def get_trace_inf(self):
        rect = self.deep_image_copy.get_rect()
        return [self.rect.x, self.rect.y, rect.width, rect.height, self.static_angle]


class TraceObstacle:
    def __init__(self, x, y, width, height, angle):
        self.color_rgb = [90, 90, 90]
        self.angle = angle
        self.step = 15
        self.counter = 0
        self.x = x
        self.y = y
        self.width, self.height = width, height

    def draw_trace(self, sc):
        for i in range(len(self.color_rgb)):
            self.color_rgb[i] = self.color_rgb[i] - self.step
        image = pygame.Surface([self.width, self.height])
        cols = (self.color_rgb[0], self.color_rgb[1], self.color_rgb[2])
        if all(list(map(lambda x: x >= 0, list(cols)))):
            image.fill(cols)
        image = pygame.transform.rotozoom(image, self.angle, 1)
        image = image.convert()
        image.set_colorkey(BLACK_COLOR)
        sc.blit(image, (self.x, self.y))
