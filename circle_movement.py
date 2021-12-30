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


class Circles(pygame.sprite.Sprite):
    def __init__(self, image, init_angle, start_x, start_y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.init_angle = init_angle
        self.rect.x = start_x
        self.rect.y = start_y
        self.color = color

    def update(self, speed_move):
        self.init_angle += speed_move
        angle = self.init_angle * math.pi / ANGLE_PI
        self.rect.x = (CONVERT_ANGLE_TO_SIDE * math.cos(angle)) + CHANGE_X_COORD
        self.rect.y = (CONVERT_ANGLE_TO_SIDE * math.sin(angle)) + CHANGE_Y_COORD
        if speed_move != IMPOSSIBLE_SPEED:
            if self.color == RED:
                traces.append(CreateTrace((self.rect.x, self.rect.y), random.choice(
                    [RED_TRAIL_COLOR_1, RED_TRAIL_COLOR_2, RED_TRAIL_COLOR_3])))
            else:
                traces.append(CreateTrace((self.rect.x, self.rect.y), random.choice(
                    [BLUE_TRAIL_COLOR_1, BLUE_TRAIL_COLOR_2, BLUE_TRAIL_COLOR_3])))

    def check_collision(self, screen, arr_with_sprites):
        for i in arr_with_sprites:
            if pygame.sprite.collide_mask(self, i):
                return True


traces = []
