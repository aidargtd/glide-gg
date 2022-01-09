import menu_for_all
from general_functions import *


def start_game(screen_size=SIZE):
    menu_for_all.Menu(screen_size).main_menu().event_loop()


if __name__ == '__main__':
    start_game()
    quit_game()
