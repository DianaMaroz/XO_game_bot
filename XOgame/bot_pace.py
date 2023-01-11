import random

from XOgame import get_mark, win

def bot_pace(field: list):
    mark = get_mark()
    if mark == 'X':
        bot_mark = 'O'
    else:
        bot_mark = 'X'
    if field[4].isdigit():
        field[4] = bot_mark
        print(field,  'бот походил')
    else:
        corner = [0, 2, 6, 8]
        random.shuffle(corner)
        # for opt in win:
        #     if (field[opt[0]] == field[opt[1]] == bot_mark) and field[opt[2]].isdigit():
        #         field[opt[2]] = bot_mark
        #         print(field, 'бот походил1')
        #         break
        #     if (field[opt[1]] == field[opt[2]] == bot_mark) and field[opt[0]].isdigit():
        #         field[opt[0]] = bot_mark
        #         print(field, 'бот походил1')
        #         break
        #     if (field[opt[0]] == field[opt[2]] == bot_mark) and field[opt[1]].isdigit():
        #         field[opt[1]] = bot_mark
        #         print(field, 'бот походил1')
        #         break
        # for opt in win:
        #     if (field[opt[0]] == field[opt[1]] == mark) and field[opt[2]].isdigit():
        #         field[opt[2]] = bot_mark
        #         print(field, 'бот походил2')
        #         break
        #     if (field[opt[1]] == field[opt[2]] == mark) and field[opt[0]].isdigit():
        #         field[opt[0]] = bot_mark
        #         print(field, 'бот походил2')
        #         break
        #     if (field[opt[0]] == field[opt[2]] == mark) and field[opt[1]].isdigit():
        #         field[opt[0]] = bot_mark
        #         print(field, 'бот походил2')
        #         break
        # for cell in corner:
        #     if field[cell].isdigit():
        #         field[cell] = bot_mark
        #         print(field, 'бот походил в угол')
        #         break
        while True:
            turn = random.randint(0, 8)
            if field[turn].isdigit():
                field[turn] = bot_mark
                print(field, 'бот походил случайно')
                break