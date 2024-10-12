import os
import platform


def welcome():
    welcome = "w e l c o m e   t o   t h e   g a m e  !".upper()
    f_title = f'\033[41m{" " * 125}'
    print(f'{f_title}{" "}\033[0m\n\n{welcome.center(125, " ")}\n\n\033[41m{" "}{f_title}\033[0m')


def lets_play():
    lets_play = "l e t ` s   p l a y   ! ! !".upper()
    f_title = f'\n\033[1;91m{"X"*100}\n'
    print(f'{f_title}\033[0m\n\033[1m{lets_play.center(100, " ")}\n{f_title}\n\033[0m')


def clear_screen():
    # Verifica se está em um terminal interativo
    if os.getenv('TERM'):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
    else:
        # Alternativa para ambientes que não suportam 'clear' ou 'cls'
        print("\n" * 100)