import pygame
import os
import sys
import math
import random

BLACK = 'black'
RED = 'red'
BLUE = 'blue'
RED_TRAIL1 = (255, 55, 0)
RED_TRAIL2 = (255, 85, 55)
RED_TRAIL3 = (255, 40, 40)

BLUE_TRAIL1 = (0, 170, 240)
BLUE_TRAIL2 = (15, 135, 255)
BLUE_TRAIL3 = (0, 190, 255)

DEEP_GRAY = (54, 54, 54)
FPS = 60
SIZE = WIDTH, HEIGHT = 600, 800
SPEED_MOVEMENT_TRUE = 5
SPEED_MOVEMENT_FALSE = -5
CONVERT_ANGLE_TO_SIDE = 100


class Particle:
    def __init__(self, pos, color):
        self.x, self.y = pos
        self.x += 10
        self.y += 10
        self.color = color
        self.vx, self.vy = random.randint(-2, 2), random.randint(-10, 0) * .1
        self.rad = 5

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.rad)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        if random.randint(0, 100) < 40:
            self.rad -= 1


class Dust:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color
        self.particles = []
        for i in range(50):
            self.particles.append(Particle(pos, color))

    def draw(self, screen):
        for i in self.particles:
            i.draw(screen)

    def update(self):
        for i in self.particles:
            i.update()
            if i.rad <= 0:
                self.particles.remove(i)


class RedCircle(pygame.sprite.Sprite):
    def __init__(self, speed=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('red_circle.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.init_red_angle = 0
        self.rect.x = 385
        self.rect.y = 585

    def update(self, speed_move):
        self.init_red_angle += speed_move
        angle_red = self.init_red_angle * math.pi / 180
        self.rect.x = (CONVERT_ANGLE_TO_SIDE * math.cos(angle_red)) + (HEIGHT // 2) - 115
        self.rect.y = (CONVERT_ANGLE_TO_SIDE * math.sin(angle_red)) + HEIGHT - 215
        dust.append(Dust((self.rect.x, self.rect.y), random.choice([RED_TRAIL1, RED_TRAIL2, RED, RED_TRAIL3])))


class BlueCircle(pygame.sprite.Sprite):
    def __init__(self, speed=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('blue_circle.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.init_blue_angle = 180
        self.rect.x = 185
        self.rect.y = 585

    def update(self, speed_move):
        self.init_blue_angle += speed_move
        angle_blue = self.init_blue_angle * math.pi / 180
        self.rect.x = (CONVERT_ANGLE_TO_SIDE * math.cos(angle_blue)) + (HEIGHT // 2 - 115)
        self.rect.y = (CONVERT_ANGLE_TO_SIDE * math.sin(angle_blue)) + (HEIGHT - 215)
        dust.append(Dust((self.rect.x, self.rect.y), random.choice([BLUE_TRAIL1, BLUE_TRAIL2, BLUE_TRAIL3])))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Game")
all_sprites = pygame.sprite.Group()

fps = 60
fps_clock = pygame.time.Clock()
red_circle = RedCircle()
blue_circle = BlueCircle()
all_sprites.add(red_circle, blue_circle)
running = True
dust = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        red_circle.update(SPEED_MOVEMENT_FALSE)
        blue_circle.update(SPEED_MOVEMENT_FALSE)
    elif keys[pygame.K_LEFT]:
        red_circle.update(SPEED_MOVEMENT_TRUE)
        blue_circle.update(SPEED_MOVEMENT_TRUE)
    screen.fill(BLACK)
    for d in dust:
        d.draw(screen)
        d.update()
    pygame.draw.circle(screen, DEEP_GRAY, (300, 600), 100, 2)
    all_sprites.draw(screen)
    pygame.display.update()
    fps_clock.tick(fps)
pygame.quit()
