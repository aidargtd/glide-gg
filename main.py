import pygame
import math

BLACK = 'black'
RED = 'red'
BLUE = 'blue'
DEEP_GRAY = (54, 54, 54)
FPS = 144
SIZE = WIDTH, HEIGHT = 600, 800
SPEED_MOVEMENT = 2


def main():
    screen = pygame.display.set_mode(SIZE)
    ratio_red = 0
    ratio_blue = 180
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        angle_red = ratio_red * math.pi / 180
        angle_blue = ratio_blue * math.pi / 180

        x_pos_red = (100 * math.cos(angle_red)) + 300
        y_pos_red = (100 * math.sin(angle_red)) + 600
        x_pos_blue = (100 * math.cos(angle_blue)) + 300
        y_pos_blue = (100 * math.sin(angle_blue)) + 600
        if keys[pygame.K_RIGHT]:
            ratio_red += SPEED_MOVEMENT
            ratio_blue += SPEED_MOVEMENT
        elif keys[pygame.K_LEFT]:
            ratio_red -= SPEED_MOVEMENT
            ratio_blue -= SPEED_MOVEMENT
        screen.fill(BLACK)
        pygame.draw.circle(screen, DEEP_GRAY, (300, 600), 100, 2)
        pygame.draw.circle(screen, RED, (x_pos_red, y_pos_red), 12)
        pygame.draw.circle(screen, BLUE, (x_pos_blue, y_pos_blue), 12)
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
