def sudoko_solver(board):

    def is_valid(row, col, num):

        for j in range(9):
            if board[row][j] == num:
                return False

        for i in range(9):
            if board[i][col] == num:
                return False

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False

        return True

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if is_valid(i, j, num):
                            board[i][j] = num
                            if backtrack():
                                return True
                            board[i][j] = '.'
                    return False
        return True

    backtrack()
