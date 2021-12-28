import pygame
from parametres import *
import circle_movement
import time

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# icon = pygame.image_load('icon.png')
# pygame.display.set_icon(icon)

all_circles = pygame.sprite.Group()
all_obstacles = pygame.sprite.Group()

fps_clock = pygame.time.Clock()

red_circle = circle_movement.RedCircle()
blue_circle = circle_movement.BlueCircle()
all_circles.add(red_circle, blue_circle)
# scores = 0


def run_game():
    # global scores
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pause()
        if keys[pygame.K_RIGHT]:
            red_circle.update(SPEED_MOVEMENT_FALSE)
            blue_circle.update(SPEED_MOVEMENT_FALSE)
        if keys[pygame.K_LEFT]:
            red_circle.update(SPEED_MOVEMENT_TRUE)
            blue_circle.update(SPEED_MOVEMENT_TRUE)
        red_circle.update(0)
        blue_circle.update(0)
        screen.fill(BLACK_COLOR)
        # print_text(f'Scores: {scores}', 10, 10, 20)
        # scores = count_scores(scores)
        pygame.draw.circle(screen, DEEP_GRAY, GRAY_CIRCLE_POSITION,
                           GRAY_CIRCLE_RADIUS, GRAY_CIRCLE_WIDTH)
        for trace in circle_movement.traces:
            trace.draw(screen)
            trace.update()

        all_circles.draw(screen)
        pygame.display.update()
        fps_clock.tick(FPS)
    return game_over()


def print_text(message, x, y, font_size=30, font_color=WHITE_COLOR, font_type='font/VeraBI.ttf'):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text('Paused. Press enter to continue', 30, 300)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False
        pygame.display.update()
        fps_clock.tick(15)


def game_over():
    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text('Game over. Press Enter to play again, Esc to exit', 20, 300, 20)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return True
        if keys[pygame.K_ESCAPE]:
            return False

        pygame.display.update()
        fps_clock.tick(15)


# def count_scores(scores):
#     time.sleep(0.5)
#     scores += 1
#     return scores


while run_game():
    pass
pygame.quit()
quit()
