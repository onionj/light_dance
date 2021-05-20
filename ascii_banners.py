import pyfiglet
from random import choice


# This function controls the animation of words


# all_font = pyfiglet.FigletFont.getFonts()  # get all pyfiglet font

best_font = [
    '3-d', '5lineoblique', '6x10',
    'acrobatic', 'alligator2', 'arrows',
    'ascii___', 'banner3-D', 'banner3',
    'banner4', 'basic', 'big',
    'briteb', 'broadway', 'bulbhead',
    'caligraphy', 'char3___',
    'charact1', 'clb6x10', 'coinstak',
    'colossal', 'contrast', 'demo_2__',
    'epic', 'fraktur', 'graceful',
    'isometric1', 'isometric2', 'isometric3', 'isometric4',
    'ivrit', 'kban', 'larry3d',
    'nancyj-fancy', 'nancyj-underlined',
    'nvscript', 'pawp', 'poison',
    'rev', 'roman', 'slant',
    'smisome1', 'speed', 'starwars',
    'univers', 'usaflag', 'whimsy',
]

Default_font = 'xbrite'
flag = 0


def random_font():
    return choice(best_font)


def create_custom_func_figlet():
    return pyfiglet.Figlet(font=Default_font)


def print_ascii_banner(text):
    print(create_custom_func_figlet().renderText(text))


def animate_ascii(text):
    global flag
    global Default_font

    text_len = len(text)

    if flag == 0:
        Default_font = random_font()

    print_ascii_banner(text[0:flag])

    if text_len == flag:
        flag = 0
        return
    flag += 1


def banner():
    print_ascii_banner('LIGHT DANCE')


def just_crate_ascii_banner(text):
    try:
        for font in best_font:
            print('-' * 50)
            print(font, '\n')
            print(pyfiglet.Figlet(font=font).renderText(text))
            input('\n\nNEXT (ENTER) , EXIT (Ctrl c) ')
    except KeyboardInterrupt:
        return
