'''
Simple light dance for Windows console  -- onionj

The main function of the program
'''

from time import sleep
from os import system

#  local import
from util import *
from ascii_banners import banner


def main_while(sleep_time):
    '''
    print animation and change color 
    '''
    while True:
        try:
            clear_cmd()
            banner()
            for _ in range(count_change_color_after_print()):
                # change CMD color:
                system(f'color {color_code()}')
                sleep(sleep_time)

        except KeyboardInterrupt:
            print('exit..')
            return


def main():
    '''
    get config and start while
    '''
    try:
        change_screen_size_cmd()
        clear_cmd()
        banner()

        main_while(get_sleep_time())

    except KeyboardInterrupt:
        print('exit..')


if __name__ == "__main__":
    main()
