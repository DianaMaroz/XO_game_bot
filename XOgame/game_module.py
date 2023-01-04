game = False
mark = 'X'

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

