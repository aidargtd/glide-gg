from general_functions import print_text
from menu_files.menu_page import MenuPage
from parametres import *
from general_functions import *


class MenuItemShopPage(MenuPage):
    def render_background(self, screen, pos=False):
        screen.fill(BLACK_COLOR)

    def render_extra(self, screen):
        x = 150
        print_text(screen, 'Магазин скинов', x, 50, FONT_SIZE_FIFTY, font_type=FONT_ROB_THIN)

    def render_image(self, screen):
        image = load_image("Items/item_shop1.png")
        pygame.transform.scale(image, (100, 200))
        rect = image.get_rect()
        mask = pygame.mask.from_surface(image)
        rect.x = 100
        rect.y = 300
