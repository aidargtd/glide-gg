# GENERAL
UNDEFINED = None

# DATABASE
DB_PATH = 'data/glide_db.db'

# TITLE OF GAME
TITLE = 'Glide game'

# COLORS (RGB)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (255, 0, 0)
BLUE_COLOR = (0, 0, 255)
DEEP_GRAY = (54, 54, 54)
WHITE_COLOR = (255, 255, 255)
RED_TRAIL_COLOR_1 = (255, 55, 0)
RED_TRAIL_COLOR_2 = (255, 85, 55)
RED_TRAIL_COLOR_3 = (255, 40, 40)
BLUE_TRAIL_COLOR_1 = (0, 170, 240)
BLUE_TRAIL_COLOR_2 = (15, 135, 255)
BLUE_TRAIL_COLOR_3 = (0, 190, 255)

# NAMES OF IMAGES
RED_CIRCLE_IMG = 'red_circle.png'
BLUE_CIRCLE_IMG = 'blue_circle.png'
BASE_WALL_IMG = "base_wall_2_1.png"

# CONSTS FOR SCREEN
SIZE = WIDTH, HEIGHT = 600, 800
START_OF_SCREEN = (0, 0)
FPS = 60

# CONSTS FOR MAKE IMG TRANSPARENT
SPECIAL_VALUE = -1

# CONSTS FOR CIRCLE TRACES
ANGLE_PI = 180
START_TRACE_RADIUS = 5
QUANTITY_TRACE_CIRCLES = 50
RADIUS_FOR_DELETE_TRACE = 0
NUM_FOR_DECREASE_RADIUS = 50
DECREASE_TRACE_RADIUS = 1
CONNECT_CIRCLE_WTH_TRC = 10
IMPOSSIBLE_SPEED = 0

# CONSTS FOR MOVEMENT CIRCLES
SPEED_MOVEMENT_TRUE = 5
SPEED_MOVEMENT_FALSE = -5
CONVERT_ANGLE_TO_SIDE = 100

# CONSTS FOR GRAY CIRCLE (along which the circles rotate)
GRAY_CIRCLE_POSITION = (300, 600)
GRAY_CIRCLE_RADIUS = 100
GRAY_CIRCLE_WIDTH = 1

# CONSTS FOR RED CIRCLE
RED_CIRCLE_START_ANGLE = 0
RED_CIRCLE_START_X = 385
RED_CIRCLE_START_Y = 585

# CONSTS FOR BLUE CIRCLE
BLUE_CIRCLE_START_ANGLE = 180
BLUE_CIRCLE_START_X = 185
BLUE_CIRCLE_START_Y = 585

# SAME CONSTS FOR CIRCLES
CHANGE_X_COORD = HEIGHT // 2 - 115
CHANGE_Y_COORD = HEIGHT - 215

# INDEXES FOR ALL OBSTACLES
INX_IMG_NAME = 0
INX_X_POS = 1
INX_Y_POS = 2
INX_X_SPEED = 3
INX_Y_SPEED = 4

# INDEXES FOR SLOWER TWIST OBSTACLE
INX_STEP_ANG_TWIST = 5
INX_BASE_ANG_TWIST = 6

# INDEXES FOR SLIDE SIDE AND LF_DOWN OBSTACLE
INX_STATIC_ANGLE = 5
BASE_X_MOVE = 0
BASE_Y_MOVE = 0
BASE_ANGLE_MOVE = 0

# INDEXES FOR SLIDE SIDE OBSTACLE
INX_Y_START_SIDE = 6
INX_Y_END_SIDE = 7
INX_STEP_SPEED_SIDE = 8

# INDEXES FOR LEFT RIGHT AND DOWN MOVING OBSTACLE
INX_Y_START_DOWN = 6
INX_Y_END_DOWN = 7
INX_STEP_SPEED_DOWN = 8
INX_LEFT_BOARD_LF = 9
INX_RIGHT_BOARD_LF = 10
INX_STEP_SPEED_LF = 11

# ARGS OF FRAMES FOR LEFT RIGHT MOVING
SIXTY_FRAMES = 60
TEN_FRAMES = 10
ZERO_FRAMES = 0
STEP_FRAME = 1

# VALUES FOR DATABASE
IMAGES = 'Images'
LEVELS = 'Levels'
LF_DOWN_OBSTACLES = 'LfDownObstacles'
SIDE_OBSTACLES = 'SideObstacles'
TWIST_OBSTACLES = 'TwistObstacles'

ID = 'id'
NAME = 'name'

ID_LEVEL = 'id_level'
ID_IMAGE = 'id_image'
X_POS = 'x_pos'
Y_POS = 'y_pos'
X_SPEED = 'x_speed'
Y_SPEED = 'y_speed'

Y_START_DOWN = 'y_start_down'
Y_END_DOWN = 'y_end_down'
SPEED_STEP_DOWN = 'speed_step_down'
LEFT_BOARD_LF = 'left_board_lf'
RIGHT_BOARD_LF = 'right_board_lf'
SPEED_STEP_LF = 'speed_step_lf'

ANGLE_STATIC = 'angle_static'
Y_START_SIDE = 'y_start_side'
Y_END_SIDE = 'y_end_side'
SPEED_STEP_SIDE = 'speed_step_side'

ANGLE_STEP = 'angle_step'
ANGLE_MOVE = 'angle_move'

TABLES = {
    IMAGES: [ID,
             NAME],

    LEVELS: [ID],

    LF_DOWN_OBSTACLES: [ID_LEVEL, ID_IMAGE,
                        X_POS, Y_POS,
                        X_SPEED, Y_SPEED, ANGLE_STATIC,
                        Y_START_DOWN,
                        Y_END_DOWN,
                        SPEED_STEP_DOWN,
                        LEFT_BOARD_LF,
                        RIGHT_BOARD_LF,
                        SPEED_STEP_LF],

    SIDE_OBSTACLES: [ID_LEVEL, ID_IMAGE,
                     X_POS, Y_POS,
                     X_SPEED, Y_SPEED,
                     ANGLE_STATIC,
                     Y_START_SIDE,
                     Y_END_SIDE,
                     SPEED_STEP_SIDE],

    TWIST_OBSTACLES: [ID_LEVEL, ID_IMAGE,
                      X_POS, Y_POS,
                      X_SPEED, Y_SPEED,
                      ANGLE_STEP,
                      ANGLE_MOVE]
}

# INDEXES FOR GET LEVEL'S OBSTACLES
INX_ID_LEVEL = 0
HIDDEN_OBSTACLE = True

# INDEXES FOR CREATING WALLS
INX_INVIZ = 0
INX_INFO_ARRAY = 1
