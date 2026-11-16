def update_board(board):
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
