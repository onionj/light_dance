
'''
founcions 
'''


from os import system
from sys import platform
from string import hexdigits
from random import randint


color_code_index = -1
FRONT_COLOR_COD = list(hexdigits)
BACK_COLOR_COD = list(hexdigits)
BACK_COLOR_COD.reverse()

speed_to_second = {
    1: 10,
    2: 7.5,
    3: 5,
    4: 2.5,
    5: 1,
    6: .5,
    7: .1,
    8: .05,
    9: .01,
    10: .005,

}


def change_screen_size_cmd(cols=140, lines=47):
    system(f'mode con: cols={cols} lines={lines}')


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
        print('\n\n\n\n')
        return
    print('\n\n\n\n')
    system('clear')


def count_change_color_after_print():
    '''
    Change the page color several times after changing the text
    '''
    return randint(1, 3)


def get_user_text():
    '''
    Get text as user
    '''
    while True:
        print(' '*5, end='')
        user_text = input('youre  text for animate: ')
        # user_text = user_text.lstrip()

        if user_text in ['']:
            print('invalid input! ,please enter a text')
            continue
        return user_text


def get_sleep_time():
    '''
    Get input from the user to set sleep time and speed
    '''
    while True:
        print(' '*5, end='')
        user_input = input('Color change speed [1-10] >> ')

        if user_input.isdigit():
            user_input = int(user_input)

            if user_input in range(1, 11):
                return speed_to_second[user_input]

        print('Invalid input')
