import pygame
from menu_files.menu_page import MenuPage
from menu_files.menu_settings_page import MenuSettingsPage
from menu_files.menu_plots_page import MenuPlotsPage
from menu_files.menu_shop_page import MenuShopPage
from menu_files.menu_sound_settings import MenuSoundPage
from menu_files.menu_levels import MenuLevelsPage
from menu_files.main_menu import MenuMainPage
from menu_files.menu_next_page_levels import MenuNextLevelsPage
from parametres import *
from load_music import *
from Button import Button
from db_functions import *


class Menu():
    def __init__(self, screen_size, action=None):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.action = action
        self.screen = pygame.display.set_mode(screen_size)
        self.menu = None
        self.scroll_y = 0
        sound(MENU_MUSIC, select_table(SETTINGS, MUSIC)[0][0])
        self.main_menu()
        self.event_loop()

    def main_menu(self):
        self.menu = MenuMainPage(self.screen)
        self.menu.add_item(BTN_LEAVE_TEXT, (50, -100), quit, font_size=FONT_SIZE_FIFTY)
        self.menu.add_item(BTN_SETTINGS_TEXT, (50, -200), self.settings_menu, font_size=FONT_SIZE_FIFTY)
        self.menu.add_item(BTN_ITEM_SHOP_TEXT, (50, -300), self.shop_menu, font_size=FONT_SIZE_FIFTY)
        self.menu.add_item(BTN_PLAY_TEXT, (50, -400), self.plots_menu, font_size=FONT_SIZE_FIFTY)

    def plots_menu(self):
        self.menu = MenuPlotsPage(self.screen)
        self.menu.add_item(BTN_PLOT_TEXT, (50, 100), self.open_plots_levels)
        self.menu.add_item(BTN_RACE_TEXT, (50, 200), self.infinity_game)
        self.menu.add_item(BTN_BACK_TEXT, (50, 300), self.main_menu)

    def shop_menu(self):
        self.menu = MenuShopPage(self.screen)
        self.menu.add_item(BTN_BACK_TEXT, (100, -100), self.main_menu)

    def infinity_game(self):
        pass

    def open_plots_levels(self):
        self.menu = MenuLevelsPage(self.screen)
        self.menu.add_item(BTN_BACK_TEXT, (490, 740), self.main_menu)
        self.menu.add_item(BTN_NEXT_PAGE_TEXT, (270, 640), self.open_next_page_levels, color=DEEP_GRAY)

    def open_next_page_levels(self):
        self.menu = MenuNextLevelsPage(self.screen)
        self.menu.add_item(BTN_BACK_TEXT, (490, 740), self.open_plots_levels)

    def sound_condition(self):
        self.menu = MenuSoundPage(self.screen)
        if select_table(SETTINGS, MUSIC)[0][0]:
            self.menu.add_item(BTN_ON_TEXT, (110, 100), self.check_on_music, BLUE_TRAIL_COLOR_3)
            sound(MENU_MUSIC, True)
        else:
            self.menu.add_item(BTN_OFF_TEXT, (110, 100), self.check_on_music, RED_TRAIL_COLOR_3)
            sound(MENU_MUSIC, False)

        if select_table(SETTINGS, VOICE)[0][0]:
            self.menu.add_item(BTN_ON_TEXT, (80, 200), self.check_on_voice, BLUE_TRAIL_COLOR_3)
        else:
            self.menu.add_item(BTN_OFF_TEXT, (80, 200), self.check_on_voice, RED_TRAIL_COLOR_3)

        if select_table(SETTINGS, SOUND_EFFECTS)[0][0]:
            self.menu.add_item(BTN_ON_TEXT, (230, 300), self.check_on_sounds_eff, BLUE_TRAIL_COLOR_3)
        else:
            self.menu.add_item(BTN_OFF_TEXT, (230, 300), self.check_on_sounds_eff, RED_TRAIL_COLOR_3)
        self.menu.add_item(BTN_BACK_TEXT, (100, -100), self.settings_menu)

    def check_on_music(self):
        update_settings_value(not select_table(SETTINGS, MUSIC)[0][0])
        self.sound_condition()

    def check_on_voice(self):
        upd_settings_voice(not select_table(SETTINGS, VOICE)[0][0])
        self.sound_condition()

    def check_on_sounds_eff(self):
        upd_settings_sound_effects(not select_table(SETTINGS, SOUND_EFFECTS)[0][0])
        self.sound_condition()

    def check_on_eff(self):
        upd_settings_val_effects(not select_table(SETTINGS, EFFECTS)[0][0])
        self.settings_menu()

    def settings_menu(self):
        self.menu = MenuSettingsPage(self.screen)
        self.menu.add_item(BTN_SOUND_TEXT, (50, 450), self.sound_condition, color=DEEP_GRAY, font_size=50)
        self.menu.add_item(BTN_BACK_TEXT, (100, -100), self.main_menu)
        if select_table(SETTINGS, EFFECTS)[0][0]:
            self.menu.add_item(BTN_ON_TEXT, (50, 370), self.check_on_eff, BLUE_TRAIL_COLOR_3)
        else:
            self.menu.add_item(BTN_OFF_TEXT, (50, 370), self.check_on_eff, RED_TRAIL_COLOR_3)

    def event_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEMOTION:
                    self.menu.hover(*event.pos)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    sound_effects(SOUND_CLICK,
                                  select_table(SETTINGS, SOUND_EFFECTS)[0][0])
                    self.menu.click(*event.pos)

            self.check_on_music
            self.menu.render()
            pygame.display.flip()
            pygame.display.update()
