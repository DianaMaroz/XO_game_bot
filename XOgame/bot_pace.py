import random

import game_module

def bot_pace(field: list):
    win = game_module.win
    mark = game_module.get_mark()
    if mark == 'X':
        bot_mark = 'O'
    else:
        bot_mark = 'X'
    if field[4].isdigit():
        field[4] = bot_mark
    else:
        corner = [0, 2, 6, 8]
        random.shuffle(corner)
        for opt in win:
            if (field[opt[0]] == field[opt[1]] == bot_mark) and field[opt[2]].isdigit():
                field[opt[2]] = bot_mark
                break
            if (field[opt[1]] == field[opt[2]] == bot_mark) and field[opt[0]].isdigit():
                field[opt[0]] = bot_mark
                break
            if (field[opt[0]] == field[opt[2]] == bot_mark) and field[opt[1]].isdigit():
                field[opt[1]] = bot_mark
                break
        for opt in win:
            if (field[opt[0]] == field[opt[1]] == mark) and field[opt[2]].isdigit():
                field[opt[2]] = bot_mark
                break
            if (field[opt[1]] == field[opt[2]] == mark) and field[opt[0]].isdigit():
                field[opt[0]] = bot_mark
                break
            if (field[opt[0]] == field[opt[2]] == mark) and field[opt[1]].isdigit():
                field[opt[0]] = bot_mark
                break
        for cell in corner:
            if field[cell].isdigit():
                field[cell] = bot_mark
                break
        while True:
            turn = random.randint(1,9)
            if field[turn].isdigit():
                field[turn]= bot_mark
