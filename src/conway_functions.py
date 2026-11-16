import numpy as np

def update_square_board(board):
    size_board = len(board)
    for i in range(size_board):
        for j in range(size_board):
            cell = board[i][j]
            number_of_live_neighbours = 0

            if board[i - 1][j - 1] == 1:
                number_of_live_neighbours += 1
            if board[i - 1][j] == 1:
                number_of_live_neighbours += 1
            if board[i - 1][j + 1] == 1:
                number_of_live_neighbours += 1
            if board[i][j - 1] == 1:
                number_of_live_neighbours += 1
            if board[i][j] == 1:
                number_of_live_neighbours += 1
            if board[i][j + 1] == 1:
                number_of_live_neighbours += 1
            if board[i + 1][j - 1] == 1:
                number_of_live_neighbours += 1
            if board[i + 1][j] == 1:
                number_of_live_neighbours += 1
            if board[i + 1][j + 1] == 1:
                number_of_live_neighbours += 1

            if cell == 0: # If the cell is dead
                if 0 <= cell <= 2 or 4 <= cell <= 8:
                    board[i][j] = 0
                elif cell == 3:
                    board[i][j] = 1
            elif cell == 1: # If the cell is alive
                if 0 <= cell <= 1 or 4 <= cell <= 8:
                    board[i][j] = 0
                elif 2 <= cell <= 3:
                    board[i][j] = 1


def update_hexagonal_board(board):
    #Padding the borad lets us the same code for all cells without getting indexation errors
    temporary_board = np.pad(board, pad_width = 1, mode = 'constant', constant_value = -1)
    size_board = len(temporary_board)


    for i in range(size_board):
        for j in range(size_board):
            cell = temporary_board[i][j]

            if cell == -1:  #If it is a padded value it should be ignored
                continue

            number_of_live_neighbours = 0
            for k in range (6):
                vertical_index = k//2 - 1
                horizontal_index = k % 2
                if vertical_index == 0 and horizontal_index == 0:
                    horizontal_index -= 1

                #Skip over padded values
                if temporary_board[i + vertical_index][j + horizontal_index] == -1:
                    continue

                number_of_live_neighbours += temporary_board[i + vertical_index][j + horizontal_index]

            #B2/S2 ruleset for the game of life
            if 0 <= number_of_live_neighbours <= 1 or 3 <= number_of_live_neighbours <= 6:
                board[i-1][j-1] = 0
            elif number_of_live_neighbours == 2:
                board[i-1][j-1] = 1

    return board