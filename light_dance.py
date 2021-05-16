
'''
Simple light dance for Windows console  -- onionj
'''

from os import system
from sys import platform
from string import hexdigits
from random import randint
from time import sleep

# local import
from ascii_banners import banner, mood


color_code_index = -1
FRONT_COLOR_COD = list(hexdigits)
BACK_COLOR_COD = list(hexdigits)
BACK_COLOR_COD.reverse()


def color_code():
    global color_code_index

    '''
    return  color code for Windows cmd \n
    Sample: 5F or 61 or 59...
     '''

    if color_code_index == 21:
        color_code_index = -1
    color_code_index += 1
    return BACK_COLOR_COD[color_code_index] + FRONT_COLOR_COD[color_code_index]


def clear_cmd():
    '''clear CMD by cls command'''

    if platform == 'win32':
        system('cls')
        return
    system('clear')


def count_change_color_after_print():
    from ascii_banners import mood

    if mood == 1:
        return randint(1, 3)
    return 1


def get_speed():
    while True:
        user_input = input('speed: [1-1000] ')

        if user_input.isdigit():
            user_input = int(user_input)

            if user_input in range(1, 1001):
                return 1001 - user_input

        print('Invalid input')


def get_sleep_time():
    speed = get_speed()
    return speed / 1000


def main_while(sleep_time):
    while True:
        try:
            clear_cmd()
            banner()
            for _ in range(count_change_color_after_print()):
                system(f'color {color_code()}')
                sleep(sleep_time)

        except KeyboardInterrupt:
            print('exit..')
            return


def main():
    try:
        clear_cmd()
        banner()
        main_while(get_sleep_time())

    except KeyboardInterrupt:
        print('exit..')


if __name__ == "__main__":
    main()
