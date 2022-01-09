from menu_files.menu_race_score import MenuRaceScore
from menu_files.menu_settings_page import MenuSettingsPage
from menu_files.menu_plots_page import MenuPlotsPage
from menu_files.menu_locker_and_shop import MenuShopAndLockerPage
from menu_files.menu_sound_settings import MenuSoundPage
from menu_files.menu_levels import MenuLevelsPage
from menu_files.main_menu import MenuMainPage
from menu_files.menu_next_page_levels import MenuNextLevelsPage
from menu_files.infinity_level_before_start import *
from menu_files.menu_locker import MenuLockerPage
from menu_files.menu_item_shop import MenuItemShopPage
from load_music import *
from general_functions import *

icon = load_image(ICON_IMG)
pygame.display.set_icon(icon)


class Menu():
    def __init__(self, screen_size, action=None):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.action = action
        self.screen = pygame.display.set_mode(screen_size)
        self.menu = None
        self.scroll_y = 0
        sound(MENU_MUSIC, select_table(SETTINGS, MUSIC)[GET_ZERO_VALUES][GET_ZERO_VALUES])

    def main_menu(self):
        self.menu = MenuMainPage(self.screen)
        self.menu.add_item(BTN_LEAVE_TEXT, (50, -100), quit_game, font_size=FONT_SIZE_FIFTY)
        self.menu.add_item(BTN_SETTINGS_TEXT, (50, -200), self.settings_menu, font_size=FONT_SIZE_FIFTY)
        self.menu.add_item(BTN_LOCKER_TEXT, (50, -300), self.menu_locker_shop, font_size=FONT_SIZE_FIFTY)
        self.menu.add_item(BTN_PLAY_TEXT, (50, -400), self.plots_menu, font_size=FONT_SIZE_FIFTY)
        return self

    def plots_menu(self):
        self.menu = MenuPlotsPage(self.screen)
        self.menu.add_item(BTN_PLOT_TEXT, (50, 100), self.open_plots_levels)
        self.menu.add_item(BTN_RACE_TEXT, (50, 200), self.start_infinity_game)
        self.menu.add_item(BTN_BACK_TEXT, (50, 300), self.main_menu)

    def menu_locker_shop(self):
        self.menu = MenuShopAndLockerPage(self.screen)
        self.menu.add_item(BTN_ITEM_SHOP_TEXT, (50, 350), self.open_item_shop, color=DEEP_GRAY)
        self.menu.add_item(BTN_LOCKER_TEXT, (50, 250), self.open_locker, color=DEEP_GRAY)
        self.menu.add_item(BTN_BACK_TEXT, (100, -100), self.main_menu)

    def open_item_shop(self):
        items = select_table(ITEM_SHOP_DB, SELECT_ALL)
        self.menu = MenuItemShopPage(self.screen)
        if items[GET_ZERO_VALUES][GET_SEC_VALUE]:
            self.menu.add_item(BTN_BUY_EQUIPMENT, (50, 300), self.add_item_to_locker, color=DEEP_GRAY)
        else:
            self.menu.add_item(BTN_PURCHASED_TEXT, (50, 300), None, color=GREEN_COLOR)
        self.menu.add_item(BTN_BACK_TEXT, (100, -100), self.menu_locker_shop)

    def open_locker(self):
        self.menu = MenuLockerPage(self.screen)
        items = select_table(LOCKERS_DB, SELECT_ALL)
        if len(items) == 2:
            if select_one_with_aspect(LOCKERS_DB, ID, FIRST_ITEM, AVAILABILITY)[GET_ZERO_VALUES]:
                self.menu.add_item(SELECTED_ITEM, (300, 250), None, GREEN_COLOR)
            else:
                self.menu.add_item(SELECT_ITEM, (300, 250), self.change_equip, DEEP_GRAY)

            if select_one_with_aspect(LOCKERS_DB, ID, SEC_ITEM, AVAILABILITY)[GET_ZERO_VALUES]:
                self.menu.add_item(SELECTED_ITEM, (300, 500), None, GREEN_COLOR)
            else:
                self.menu.add_item(SELECT_ITEM, (300, 500), self.change_equip_sec, DEEP_GRAY)

        self.menu.add_item(BTN_BACK_TEXT, (100, -100), self.menu_locker_shop)

    def change_equip(self):
        update_availability_item_in_locker(False, SEC_ITEM)
        update_availability_item_in_locker(True, FIRST_ITEM)
        self.open_locker()

    def add_item_to_locker(self):
        items = select_table(ITEM_SHOP_DB, SELECT_ALL)
        balance = select_one_with_aspect(USERS, ID, FIRST_ITEM, COINS_AMOUNT)[GET_ZERO_VALUES]
        price = items[GET_ZERO_VALUES][GET_THIRD_VALUE]
        if balance - price >= BALANCE_MIN:
            update_availability_item_in_shop()
            upd_balance(balance - price)
            insert_to_locker(SEC_ITEM, items[GET_ZERO_VALUES][GET_FIRST_VALUES], GET_ZERO_VALUES, items[0][4])
        self.open_item_shop()

    def start_infinity_game(self):
        self.menu = BeforeInfinityLevel(self.screen)
        self.menu.add_item(BTN_START_RACE, (30, 300), self.menu.check_name, font_size=FONT_FORTY_SIZE, color=DEEP_GRAY)
        self.menu.add_item(BTN_BACK_TEXT, (100, -100), self.plots_menu)

    def open_plots_levels(self):
        self.menu = MenuLevelsPage(self.screen)
        self.menu.add_item(BTN_BACK_TEXT, (490, 740), self.plots_menu)
        self.menu.add_item(BTN_NEXT_PAGE_TEXT, (270, 640), self.open_next_page_levels, color=DEEP_GRAY)

    def open_next_page_levels(self):
        self.menu = MenuNextLevelsPage(self.screen)
        self.menu.add_item(BTN_BACK_TEXT, (490, 740), self.open_plots_levels)

    def sound_condition(self):
        self.menu = MenuSoundPage(self.screen)
        if select_table(SETTINGS, MUSIC)[GET_ZERO_VALUES][GET_ZERO_VALUES]:
            self.menu.add_item(BTN_ON_TEXT, (110, 100), self.check_on_music, BLUE_TRAIL_COLOR_3)
            sound(MENU_MUSIC, True)
        else:
            self.menu.add_item(BTN_OFF_TEXT, (110, 100), self.check_on_music, RED_TRAIL_COLOR_3)
            sound(MENU_MUSIC, False)

        if select_table(SETTINGS, VOICE)[GET_ZERO_VALUES][GET_ZERO_VALUES]:
            self.menu.add_item(BTN_ON_TEXT, (80, 200), self.check_on_voice, BLUE_TRAIL_COLOR_3)
        else:
            self.menu.add_item(BTN_OFF_TEXT, (80, 200), self.check_on_voice, RED_TRAIL_COLOR_3)

        if select_table(SETTINGS, SOUND_EFFECTS)[GET_ZERO_VALUES][GET_ZERO_VALUES]:
            self.menu.add_item(BTN_ON_TEXT, (230, 300), self.check_on_sounds_eff, BLUE_TRAIL_COLOR_3)
        else:
            self.menu.add_item(BTN_OFF_TEXT, (230, 300), self.check_on_sounds_eff, RED_TRAIL_COLOR_3)
        self.menu.add_item(BTN_BACK_TEXT, (100, -100), self.settings_menu)

    def check_on_music(self):
        update_settings_value(not select_table(SETTINGS, MUSIC)[GET_ZERO_VALUES][GET_ZERO_VALUES])
        self.sound_condition()

    def change_equip_sec(self):
        update_availability_item_in_locker(False, FIRST_ITEM)
        update_availability_item_in_locker(True, SEC_ITEM)
        self.open_locker()

    def check_on_voice(self):
        upd_settings_voice(not select_table(SETTINGS, VOICE)[GET_ZERO_VALUES][GET_ZERO_VALUES])
        self.sound_condition()

    def check_on_sounds_eff(self):
        upd_settings_sound_effects(not select_table(SETTINGS, SOUND_EFFECTS)[GET_ZERO_VALUES][GET_ZERO_VALUES])
        self.sound_condition()

    def check_on_eff(self):
        upd_settings_val_effects(not select_table(SETTINGS, EFFECTS)[GET_ZERO_VALUES][GET_ZERO_VALUES])
        self.settings_menu()

    def settings_menu(self):
        self.menu = MenuSettingsPage(self.screen)
        self.menu.add_item(BTN_SOUND_TEXT, (50, 450), self.sound_condition, color=DEEP_GRAY, font_size=FONT_SIZE_FIFTY)
        self.menu.add_item(BTN_BACK_TEXT, (100, -100), self.main_menu)
        if select_table(SETTINGS, EFFECTS)[GET_ZERO_VALUES][GET_ZERO_VALUES]:
            self.menu.add_item(BTN_ON_TEXT, (50, 370), self.check_on_eff, BLUE_TRAIL_COLOR_3)
        else:
            self.menu.add_item(BTN_OFF_TEXT, (50, 370), self.check_on_eff, RED_TRAIL_COLOR_3)

    def race_score_menu(self, name, score):
        self.menu = MenuRaceScore(self.screen, name, score)
        self.menu.add_item(BTN_MAIN_MENU_TEXT, (50, -100), self.main_menu)
        return self

    def event_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                elif event.type == pygame.MOUSEMOTION:
                    self.menu.hover(*event.pos)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    sound_effects(SOUND_CLICK,
                                  select_table(SETTINGS, SOUND_EFFECTS)[GET_ZERO_VALUES][GET_ZERO_VALUES])
                    self.menu.click(*event.pos)
                self.menu.extra_event_handler(event)
            self.check_on_music
            self.menu.render()
            pygame.display.flip()
            pygame.display.update()
