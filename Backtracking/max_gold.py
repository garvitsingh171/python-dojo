def getMaximumGold(grid):
    rows = len(grid)
    cols = len(grid[0])

    max_gold = 0

    # Directions: up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(r, c):
        # If out of bounds OR cell is 0 → stop
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
            return 0

        # Take current gold
        current_gold = grid[r][c]

        # Mark visited (IMPORTANT)
        grid[r][c] = 0

        max_path_gold = 0

        # Explore all 4 directions
        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc

            gold = dfs(new_r, new_c)
            max_path_gold = max(max_path_gold, gold)

        # Backtrack (restore value)
        grid[r][c] = current_gold

        return current_gold + max_path_gold

    # Try starting from every cell
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                max_gold = max(max_gold, dfs(i, j))

    return max_gold
