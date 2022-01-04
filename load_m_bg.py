import pygame
from parametres import *
pygame.init()

kosmo_imgs = []

for i in range(FIRST_FRAME, LAST_FRAME):
    path = f'{KOSMO_BGD}{i}{PNG}'
    kosmo_imgs.append(pygame.image.load(path))
