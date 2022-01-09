from general_functions import print_text
from menu_files.menu_page import MenuPage
from parametres import FONT_FORTY_SIZE, FONT_ROB_THIN, WHITE_COLOR


class MenuRaceScore(MenuPage):
    def __init__(self, screen, name, score):
        super().__init__(screen)
        self.score = score
        self.name = name

    def render_extra(self, screen):
        print_text(screen, f'{self.name}, счёт: {self.score}', 50, 50, FONT_FORTY_SIZE, WHITE_COLOR,
                   font_type=FONT_ROB_THIN)
