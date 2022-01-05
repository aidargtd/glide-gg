from abc import abstractmethod
import pygame

class AnimatedBackground:
    def __init__(self, screen):
        self.screen = screen
        self.all_sprites = self.init_sprites()

    @abstractmethod
    def init_sprites(self) -> pygame.sprite.Group:
        pass

    def render(self):
        self.all_sprites.update()
        self.screen.fill((30, 30, 30))
        self.all_sprites.draw(self.screen)
