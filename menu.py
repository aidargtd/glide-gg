import pygame
from menu_files.menu_page import MenuPage
from menu_files.menu_settings_page import MenuSettingsPage
from menu_files.menu_plots_page import MenuPlotsPage
from menu_files.menu_shop_page import MenuShopPage
from menu_files.menu_sound_settings import MenuSoundPage
from menu_files.menu_levels import MenuLevelsPage
from parametres import *
from Button import Button

dict_changing_values = {'music': True, 'voice': True, 'sound_effects': True, 'effects': True}


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
        self.menu.add_item('играть', (50, -400), self.plots_menu)

    def plots_menu(self):
        self.menu = MenuPlotsPage(self.screen)
        self.menu.add_item('сюжет', (50, 100), self.open_plots_levels)
        self.menu.add_item('гонка', (50, 200), self.infinity_game)
        self.menu.add_item('назад', (50, 300), self.main_menu)

    def shop_menu(self):
        self.menu = MenuShopPage(self.screen)
        self.menu.add_item('назад', (100, -100), self.main_menu)

    def infinity_game(self):
        pass

    def open_plots_levels(self):
        self.menu = MenuLevelsPage(self.screen)
        self.menu.add_item('назад', (50, 300), self.main_menu)

    def sound_condition(self):
        self.menu = MenuSoundPage(self.screen)
        if dict_changing_values['music']:
            self.menu.add_item('вкл', (110, 100), self.check_on_music, BLUE_TRAIL_COLOR_3)
        else:
            self.menu.add_item('выкл', (110, 100), self.check_on_music, RED_TRAIL_COLOR_3)
        if dict_changing_values['voice']:
            self.menu.add_item('вкл', (80, 200), self.check_on_voice, BLUE_TRAIL_COLOR_3)
        else:
            self.menu.add_item('выкл', (80, 200), self.check_on_voice, RED_TRAIL_COLOR_3)
        if dict_changing_values['sound_effects']:
            self.menu.add_item('вкл', (230, 300), self.check_on_sounds_eff, BLUE_TRAIL_COLOR_3)
        else:
            self.menu.add_item('выкл', (230, 300), self.check_on_sounds_eff, RED_TRAIL_COLOR_3)
        self.menu.add_item('назад', (100, -100), self.settings_menu)

    def check_on_music(self):
        dict_changing_values['music'] = not dict_changing_values['music']
        self.sound_condition()

    def check_on_voice(self):
        dict_changing_values['voice'] = not dict_changing_values['voice']
        self.sound_condition()

    def check_on_sounds_eff(self):
        dict_changing_values['sound_effects'] = not dict_changing_values['sound_effects']
        self.sound_condition()

    def check_on_eff(self):
        dict_changing_values['effects'] = not dict_changing_values['effects']
        self.settings_menu()

    def settings_menu(self):
        self.menu = MenuSettingsPage(self.screen)
        self.menu.add_item('звук', (50, 300), self.sound_condition)
        self.menu.add_item('назад', (100, -100), self.main_menu)
        if dict_changing_values['effects']:
            self.menu.add_item('вкл', (50, 450), self.check_on_eff, BLUE_TRAIL_COLOR_3)
        else:
            self.menu.add_item('выкл', (50, 450), self.check_on_eff, RED_TRAIL_COLOR_3)

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