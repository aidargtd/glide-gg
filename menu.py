import sys
import pygame
from menu_page import MenuPage
from menu_item import MenuItem


class Menu():
    def __init__(self, screen_size):
        pygame.init()
        pygame.display.set_caption('Меню')
        self.screen = pygame.display.set_mode(screen_size)
        self.menu = None
        self.main_menu()
        self.event_loop()

    def main_menu(self):
        self.menu = MenuPage(self.screen)
        # элементы меню добавляются снизу вверх
        self.menu.add_item(MenuItem('Выход', self.quit))
        self.menu.add_item(MenuItem('Настройки', self.settings_menu))
        self.menu.add_item(MenuItem('Играть'))

    def settings_menu(self):
        self.menu = MenuPage(self.screen)
        self.menu.add_item(MenuItem('Назад', self.main_menu))

    def quit(self):
        pygame.quit()
        sys.exit()

    def event_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.MOUSEMOTION:
                    self.menu.hover(*event.pos)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.menu.click(*event.pos)
            self.menu.render()
            pygame.display.update()


if __name__ == '__main__':
    Menu((600, 800))
