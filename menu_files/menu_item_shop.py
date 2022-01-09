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
        x_for_item_name = 50
        y_for_item_name = -200
        x_for_item_price = 350
        y_for_item_price = -100
        print_text(screen, ITEM_SHOP_TEXT, x=50, y=40, font_size=FONT_FORTY_SIZE, font_color=DEEP_GRAY,
                   font_type=FONT_ROB_THIN)
        coins = str(select_one_with_aspect(USERS, ID, FIRST_ITEM, COINS_AMOUNT)[GET_ZERO_VALUES])
        print_text(screen, f'{BALANCE_TEXT} {coins}', x=350, y=40, font_size=FONT_FORTY_SIZE, font_color=DEEP_GRAY,
                   font_type=FONT_ROB_THIN)
        items = select_table(ITEM_SHOP_DB, SELECT_ALL)

        for i in range(len(items)):
            y_for_item_name += INCREASE_ITEMS_Y2
            y_for_item_price += INCREASE_ITEMS_Y2
            print_text(screen, f'{ITEM_NAME_TEXT} {items[i][GET_FOURTH_VALUE]}', x=x_for_item_name, y=y_for_item_name,
                       font_size=FONT_THIRTY_SIZE, font_color=WHITE_COLOR, font_type=FONT_ROB_THIN)
            print_text(screen, f'{ITEM_PRICE_TEXT} {items[i][GET_THIRD_VALUE]}', x=x_for_item_price, y=y_for_item_price,
                       font_size=FONT_THIRTY_SIZE, font_color=WHITE_COLOR, font_type=FONT_ROB_THIN)
            image = load_image(items[i][GET_FIRST_VALUES])
            rect = image.get_rect()
            start_x_items += INCREASE_ITEMS_X1
            start_y_items += INCREASE_ITEMS_Y1
            rect.x = start_x_items
            rect.y = start_y_items
            screen.blit(image, rect)
