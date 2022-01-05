import pygame
from background.animated_background import AnimatedBackground


class Square(pygame.sprite.Sprite):
    def __init__(self, angle, x, y, h, size, color=(70, 70, 70)):
        super().__init__()
        self.image = pygame.Surface((size, size + 2 * h), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, size, size), 0)
        self.rect = self.image.get_rect(center=(x, y))
        self.orig_image = self.image
        self.angle = angle
        self.rotate()

    def update(self):
        self.angle -= 1
        self.rotate()

    def rotate(self):
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)


class Whirlpool(AnimatedBackground):
    def init_sprites(self) -> pygame.sprite.Group:
        return pygame.sprite.Group(list(self.generate_squares()))

    def generate_squares(self):
        rect = self.screen.get_rect()
        center_x = rect.w // 2
        center_y = rect.h // 2
        for angle in range(0, 5 * 360, 21):
            radius = angle // 5
            size = angle // 40
            yield Square(angle, center_x, center_y, radius, size)