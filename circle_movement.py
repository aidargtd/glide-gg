import math
import random
from parametres import *
from general_functions import *


class ParticleTrace:
    def __init__(self, pos, color):
        self.x, self.y = pos
        self.x += CONNECT_CIRCLE_WTH_TRC
        self.y += CONNECT_CIRCLE_WTH_TRC
        self.color = color
        self.change_fact_x, self.change_fact_y = \
            random.randint(-2, 2), random.randint(-10, 0) * .1
        self.radius = START_TRACE_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.x += self.change_fact_x
        self.y += self.change_fact_y
        if random.randint(0, 100) < NUM_FOR_DECREASE_RADIUS:
            self.radius -= DECREASE_TRACE_RADIUS


class CreateTrace:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color
        self.particles = []
        for _ in range(QUANTITY_TRACE_CIRCLES):
            self.particles.append(ParticleTrace(pos, color))

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)

    def update(self):
        for particle in self.particles:
            particle.update()
            if particle.radius <= RADIUS_FOR_DELETE_TRACE:
                self.particles.remove(particle)


class RedCircle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(RED_CIRCLE_IMG)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.init_red_angle = RED_CIRCLE_START_ANGLE
        self.rect.x = RED_CIRCLE_START_X
        self.rect.y = RED_CIRCLE_START_Y

    def update(self, speed_move):
        self.init_red_angle += speed_move
        angle_red = self.init_red_angle * math.pi / ANGLE_PI
        self.rect.x = (CONVERT_ANGLE_TO_SIDE * math.cos(angle_red)) + CHANGE_X_COORD
        self.rect.y = (CONVERT_ANGLE_TO_SIDE * math.sin(angle_red)) + CHANGE_Y_COORD
        if speed_move != IMPOSSIBLE_SPEED:
            traces.append(CreateTrace((self.rect.x, self.rect.y), random.choice(
                [RED_TRAIL_COLOR_1, RED_TRAIL_COLOR_2, RED_TRAIL_COLOR_3])))


class BlueCircle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(BLUE_CIRCLE_IMG)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.init_blue_angle = BLUE_CIRCLE_START_ANGLE
        self.rect.x = BLUE_CIRCLE_START_X
        self.rect.y = BLUE_CIRCLE_START_Y

    def update(self, speed_move):
        self.init_blue_angle += speed_move
        angle_blue = self.init_blue_angle * math.pi / ANGLE_PI
        self.rect.x = (CONVERT_ANGLE_TO_SIDE * math.cos(angle_blue)) + CHANGE_X_COORD
        self.rect.y = (CONVERT_ANGLE_TO_SIDE * math.sin(angle_blue)) + CHANGE_Y_COORD
        if speed_move != IMPOSSIBLE_SPEED:
            traces.append(CreateTrace((self.rect.x, self.rect.y), random.choice(
                [BLUE_TRAIL_COLOR_1, BLUE_TRAIL_COLOR_2, BLUE_TRAIL_COLOR_3])))


traces = []
# pygame.init()
# screen = pygame.display.set_mode(SIZE)
# pygame.display.set_caption(TITLE)
# all_sprites = pygame.sprite.Group()
#
# fps_clock = pygame.time.Clock()
# red_circle = RedCircle()
# blue_circle = BlueCircle()
# all_sprites.add(red_circle, blue_circle)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_RIGHT]:
#         red_circle.update(SPEED_MOVEMENT_FALSE)
#         blue_circle.update(SPEED_MOVEMENT_FALSE)
#     elif keys[pygame.K_LEFT]:
#         red_circle.update(SPEED_MOVEMENT_TRUE)
#         blue_circle.update(SPEED_MOVEMENT_TRUE)
#     screen.fill(BLACK_COLOR)
#
#     pygame.draw.circle(screen, DEEP_GRAY, GRAY_CIRCLE_POSITION, GRAY_CIRCLE_RADIUS, GRAY_CIRCLE_WIDTH)
#
#     for trace in traces:
#         trace.draw(screen)
#         trace.update()
#
#     all_sprites.draw(screen)
#     pygame.display.update()
#     fps_clock.tick(FPS)
# pygame.quit()
