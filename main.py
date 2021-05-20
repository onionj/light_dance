'''
Simple light dance for Windows console  -- onionj

The main function of the program
'''

from time import sleep
from os import system

#  local import
from util import *
from ascii_banners import *


def main():
    '''
    get config and start while
    '''
    try:
        change_screen_size_cmd()
        clear_cmd()
        banner()

        if get_animation_or_crater():  # if user choice is animation:
            main_while(get_user_text(), get_sleep_time())
            return
        just_crate_ascii_banner(get_user_text())

    except KeyboardInterrupt:
        print('exit..')


if __name__ == "__main__":
    main()
