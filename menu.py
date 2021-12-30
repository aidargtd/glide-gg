import sys
import pygame
from menu_page import MenuPage
from menu_item import MenuItem
from Button import *


class Menu():
    def __init__(self, screen_size, action=None):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.action = action
        self.screen = pygame.display.set_mode(screen_size)
        self.menu = None
        self.main_menu()
        self.event_loop()

    def main_menu(self):
        self.menu = MenuPage(self.screen)
        self.menu.add_item(MenuItem('выход', quit))
        self.menu.add_item(MenuItem('настройки', self.settings_menu))
        self.menu.add_item(MenuItem('играть', self.action))

    def settings_menu(self):
        self.menu = MenuPage(self.screen)
        self.menu.add_item(MenuItem('назад', self.main_menu))

    def event_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEMOTION:
                    self.menu.hover(*event.pos)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.menu.click(*event.pos)
            self.menu.render()

            pygame.display.update()