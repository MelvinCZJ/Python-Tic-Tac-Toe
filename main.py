board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

winner = '-'
turn = 'x'

def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def check_rows():
    global winner
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    if row1:
        winner = board[0]
    if row2:
        winner = board[3]
    if row3:
        winner = board[6]
    return row1 or row2 or row3

def check_columns():
    global winner
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'
    if column1:
        winner = board[0]
    if column2:
        winner = board[3]
    if column3:
        winner = board[6]
    return column1 or column2 or column3

def check_diagonals():
    global winner
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'
    if diagonal1 or diagonal2:
        winner = board[4]
    return diagonal1 or diagonal2

def check_win():
    return check_rows() or check_columns() or check_diagonals()

def flip_turn():
    global turn
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'

def handle_turn():
    global  turn
    tile = int(input("Please choose a tile from 1 to 9: ")) - 1
    if tile < 0 or tile > 8:
        return False
    if board[tile] == '-':
        board[tile] = turn
        return True
    else:
        print("Invalid tile! Please choose another tile!")
        return False

def play_game():
    while winner == '-':
        display_board()
        while not handle_turn():
            display_board()
        flip_turn()
        check_win()
    display_board()
    print("The winner is " + winner + "!")

play_game()