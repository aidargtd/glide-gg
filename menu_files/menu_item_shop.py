from general_functions import print_text
from menu_files.menu_page import MenuPage
from parametres import *
from general_functions import *


class MenuItemShopPage(MenuPage):

    def render_background(self, screen, pos=False):
        screen.fill(BLACK_COLOR)

    def render_extra(self, screen):
        start_x_items = -100
        start_y_items = -50
        x = 50
        x_for_item_name = 50
        y_for_item_name = -200
        x_for_item_price = 350
        y_for_item_price = -100
        print_text(screen, ITEM_SHOP_TEXT, x, 40, FONT_FORTY_SIZE, DEEP_GRAY, FONT_ROB_THIN)
        coins = str(select_one_with_aspect(USERS, ID, 1, COINS_AMOUNT)[0])
        print_text(screen, f'{BALANCE_TEXT} {coins}', 350, 40, FONT_FORTY_SIZE, DEEP_GRAY, FONT_ROB_THIN)
        items = select_table(ITEM_SHOP_DB, SELECT_ALL)
        for i in range(len(items)):
            y_for_item_name += 300
            y_for_item_price += 300
            print_text(screen, f'{ITEM_NAME_TEXT} {items[i][4]}', x_for_item_name, y_for_item_name,
                       FONT_THIRTY_SIZE, WHITE_COLOR, FONT_ROB_THIN)
            print_text(screen, f'{ITEM_PRICE_TEXT} {items[i][3]}', x_for_item_price, y_for_item_price,
                       FONT_THIRTY_SIZE, WHITE_COLOR, FONT_ROB_THIN)
            image = load_image(items[i][1])
            rect = image.get_rect()
            start_x_items += 200
            start_y_items += 200
            rect.x = start_x_items
            rect.y = start_y_items
            screen.blit(image, rect)
