def max_gold(grid):
    rows = len(grid)
    cols = len(grid[1])

    max_gold = 0

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def backtrack(i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
            return 0

        max_path_gold = 0

        curr_gold = grid[i][j]

        grid[i][j] == 0

        for r, c in directions:
            max_path_gold = max(max_path_gold, backtrack(i+r, j+c))

        grid[i][j] = curr_gold

        return curr_gold + max_path_gold

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                max_gold = max(max_gold, backtrack(i, j))

    return max_gold


n, m = list(map(int, input().split()))

grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

print(max_gold(grid))
