import pygame
from general_functions import *


class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(MOUSE_PNG)
        self.rect = self.image.get_rect()

    def update(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
