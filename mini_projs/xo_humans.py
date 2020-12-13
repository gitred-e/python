import os

board = [' ' for i in range(0, 10)]
temp = 0


def start():
    update_screen()
    while True:
        if player_move('X'):
            if check_winner(board, 'X'):
                print('\n..."X" won the game...\n')
                break
            elif check_draw(board):
                print('\n...Tie Game...\n')
                break

        if player_move('O'):
            if check_winner(board, 'O'):
                print('\n..."O" won the game...\n')
                break
            elif check_draw(board):
                print('\n...Tie Game...\n')
                break


def update_screen():
    os.system('cls')
    print('*** Welcome to Tic-Tac-Toe ***\n')
    draw_board(board)


def draw_board(bo):
    print('', bo[1], '|', bo[2], '|', bo[3])
    print('-----------')
    print('', bo[4], '|', bo[5], '|', bo[6])
    print('-----------')
    print('', bo[7], '|', bo[8], '|', bo[9])


def player_move(player):
    go_on = True
    while go_on:
        pos = input(f'\n>>> Player "{player}" <<<, Choose your position (1 to 9):')
        try:
            pos = int(pos)
            if pos > 0 and pos < 10:
                if check_empty(pos):
                    go_on = False
                    insert(player, pos)
                else:
                    update_screen()
                    print(f'\n___ Sorry Player "{player}", This position is occupied. ___')
            else:
                update_screen()
                print(f'\n___ Player "{player}", Choose your position within the given range. ___')
        except:
            update_screen()
            print(f'\n___ Player "{player}", Your position should be a number. ___')
    return True


def check_empty(pos):
    if board[pos] == ' ':
        return True


def insert(player, pos):
    board[pos] = player
    update_screen()


def check_winner(bo, player):
    if bo[1] == player and bo[2] == player and bo[3] == player:
        return True
    elif bo[4] == player and bo[5] == player and bo[6] == player:
        return True
    elif bo[7] == player and bo[8] == player and bo[9] == player:
        return True
    elif bo[1] == player and bo[4] == player and bo[7] == player:
        return True
    elif bo[2] == player and bo[5] == player and bo[8] == player:
        return True
    elif bo[3] == player and bo[6] == player and bo[9] == player:
        return True
    elif bo[1] == player and bo[5] == player and bo[9] == player:
        return True
    elif bo[3] == player and bo[5] == player and bo[7] == player:
        return True
    return False


def check_draw(bo):
    tem = 0
    for i in range(1, 10):
        if bo[i] != ' ':
            tem += 1
    if tem == 9:
        return True
    else:
        return False


while True:
    ask = input('\n>>> Press \'Enter\' to PLAY or Press \'Any Key + Enter\' to QUIT the game: <<<')
    temp += 1
    if ask == '' and temp == 1:
        start()
    elif ask == '' and temp > 1:
        board = [' ' for i in range(0, 10)]
        start()
    else:
        break
