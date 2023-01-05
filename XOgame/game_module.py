game = False
mark = 'X'
field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

def get_game():
    global game
    return game

def set_game():
    global game
    if game:
        game = False
    else:
        game = True
    return game

def get_mark():
    global mark
    return mark

def set_mark():
    global mark
    if mark == 'X':
        mark = 'O'
    else:
        mark = 'X'
    return mark

