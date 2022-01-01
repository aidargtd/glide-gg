import pygame

pygame.init()

kosmo_imgs = []

for i in range(1, 40):
    path = f'bg_kosmo/kosmo{i}.png'
    kosmo_imgs.append(pygame.image.load(path))
