def word_search(board, word):
    rows = len(board)
    cols = len(board[0])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def backtrack(i, j, index):
        if index == len(word):
            return True

        if i < 0 or j < 0 or i >= rows or j >= cols:
            return False

        if board[i][j] != word[index]:
            return False

        curr_lett = board[i][j]

        board[i][j] = '#'

        for r, c in directions:
            if backtrack(i+r, j+c, index+1):
                board[i][j] = curr_lett
                return True

        board[i][j] = curr_lett

        return False

    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True

    return False
