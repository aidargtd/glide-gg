import os
import sys
import pygame
from parametres import *


# Функции для загрузки спрайтов (сделали Айдар и Карим) Придумали как это реализовать
def load_image(name):
    fullname = os.path.join('pictures', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# Функции для печати текста (сделали Айдар и Карим) Придумали как это реализовать
def print_text(screen, message, x, y, font_size=30, font_color=WHITE_COLOR, font_type='font/VeraBI.ttf'):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))
