import pygame
from background.animated_background import AnimatedBackground


class Square(pygame.sprite.Sprite):
    def __init__(self, pos, max_size, angle_incr, scale_mul, size=30, color=(70, 70, 70), border=4):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, size, size), border)
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.angle = 60
        self.scale = 1
        self.angle_incr = angle_incr
        self.scale_mul = scale_mul
        self.max_size = max_size

    def over_screen(self):
        w, h = self.max_size
        return self.rect.w > w and self.rect.h > h

    def update(self):
        if self.over_screen():
            self.kill()
        else:
            self.angle += self.angle_incr
            self.scale *= self.scale_mul
            self.rotate()

    def rotate(self):
        self.image = pygame.transform.rotozoom(self.orig_image, self.angle, self.scale)
        self.rect = self.image.get_rect(center=self.rect.center)


class BackgroundCenterSquares(AnimatedBackground):
    def __init__(self, screen, angle_incr, scale_mul):
        self.angle_incr = angle_incr
        self.scale_mul = scale_mul
        rect = screen.get_rect()
        self.spawn_pos = (rect.w // 2, rect.h // 2)
        self.max_size = (rect.w, rect.h)
        super().__init__(screen)

    def new_square(self):
        return Square(self.spawn_pos, self.max_size, self.angle_incr, self.scale_mul)

    def add_square(self):
        if list(self.all_sprites)[-1].scale > 1.5:
            self.all_sprites.add(self.new_square())

    def init_sprites(self) -> pygame.sprite.Group:
        return pygame.sprite.Group(self.new_square())

    def render(self):
        self.add_square()
        super().render()


