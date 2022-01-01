import pygame
from menu_page import MenuPage
from menu_settings_page import MenuSettingsPage
from menu_plots_page import MenuPlotsPage
from menu_shop_page import MenuShopPage
from parametres import TITLE


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
        self.menu.add_item('выход', (50, -100), quit)
        self.menu.add_item('настройки', (50, -200), self.settings_menu)
        self.menu.add_item('магазин', (50, -300), self.shop_menu)
        self.menu.add_item('играть', (50, -400), self.action)

    def plots_menu(self):
        self.menu = MenuPlotsPage(self.screen)
        self.menu.add_item('назад', (100, -100), self.main_menu)

    def shop_menu(self):
        self.menu = MenuShopPage(self.screen)
        self.menu.add_item('назад', (100, -100), self.main_menu)

    def settings_menu(self):
        self.menu = MenuSettingsPage(self.screen)
        self.menu.add_item('звук', (50, 300), self.main_menu)
        self.menu.add_item('назад', (100, -100), self.main_menu)

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


if __name__ == '__main__':
    Menu((600, 800))
