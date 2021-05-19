import pyfiglet
from random import choice

# This function controls the animation of words

choices_font = 'xbrite'
flag = 0


def random_font():
    return choice(pyfiglet.FigletFont.getFonts())


def create_custom_func_figlet():
    return pyfiglet.Figlet(font=choices_font)


def print_ascii_banner(text):
    print(create_custom_func_figlet().renderText(text))


def animate_ascii(text):
    global flag
    global choices_font

    text_len = len(text)

    if flag == 0:
        choices_font = random_font()

    print_ascii_banner(text[0:flag+1])

    if text_len == flag:
        flag = 0
        return
    flag += 1


def banner():
    print_ascii_banner('LIGHT DANCE')
