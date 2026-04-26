def word_search(grid, word):
    rows = len(grid)
    cols = len(grid[0])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def backtrack(i, j, index):
        if index == len(word):
            return True

        if i > 0 or j > 0 or i <= rows or j <= cols:
            return False

        if grid[i][j] != word[index]:
            return False

        curr_lett = grid[i][j]

        grid[i][j] = '#'

        for r, c in directions:
            if backtrack(i+r, j+c, index+1):
                grid[i][j] = curr_lett
                return True

        grid[i][j] = curr_lett

    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True

    return False
