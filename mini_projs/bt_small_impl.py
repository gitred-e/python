# Non-GUI version

import os

board = [
    [0, 0,  0, 0],
    [0, 1,  0, 0],

    [0, 0,  3, 0],
    [0, 0,  0, 0]
]


def draw_board(bo):

    print(bo[0][0], ' | ', bo[0][1], ' | ', bo[0][2], ' | ', bo[0][3])
    print('--------------------')
    print(bo[1][0], ' | ', bo[1][1], ' | ', bo[1][2], ' | ', bo[1][3])
    print('--------------------')
    print(bo[2][0], ' | ', bo[2][1], ' | ', bo[2][2], ' | ', bo[2][3])
    print('--------------------')
    print(bo[3][0], ' | ', bo[3][1], ' | ', bo[3][2], ' | ', bo[3][3])


def solve(bo):

    find = find_empty(bo)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 5):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0

    return False


def find_empty(bo):

    for i in range(len(bo[0])):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return False


def valid(bo, num, pos):

    for i in range(len(bo[0])):  # Row Check
        if bo[pos[0]][i] == num and i != pos[1]:
            return False

    for i in range(len(bo[0])):  # Column check
        if bo[i][pos[1]] == num and i != pos[0]:
            return False

    # Check Box
    box_x = pos[1] // 2
    box_y = pos[0] // 2

    for i in range(box_y * 2, box_y * 2 + 2):
        for j in range(box_x * 2, box_x * 2 + 2):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


os.system('clear')
print(' SUDOKU Puzzle:\n')
draw_board(board)

if solve(board):
    print('\n\n Solved:\n')
    draw_board(board)
    print('\n')
else:
    print('\n No Solution\n')
