from general_functions import print_text
from menu_files.menu_page import MenuPage
from parametres import *
from db_functions import *
from general_functions import *


class MenuLockerPage(MenuPage):
    def render_background(self, screen, pos=False):
        screen.fill(BLACK_COLOR)

    def render_extra(self, screen):
        x = 50
        print_text(screen, LOCKER_TEXT, x, 40, FONT_FORTY_SIZE, DEEP_GRAY, FONT_ROB_THIN)
        items = select_table(LOCKERS_DB, SELECT_ALL)
        start_x_items = 100
        start_y_items = -50
        x_for_item_name = 50
        y_for_item_name = -200
        for i in range(len(items)):
            y_for_item_name += 300

            print_text(screen, f'{ITEM_NAME_TEXT} {items[i][3]}', x_for_item_name, y_for_item_name,
                       FONT_THIRTY_SIZE, WHITE_COLOR, FONT_ROB_THIN)
            image = load_image(items[i][1])
            rect = image.get_rect()
            start_y_items += 250
            rect.x = start_x_items
            rect.y = start_y_items
            screen.blit(image, rect)
