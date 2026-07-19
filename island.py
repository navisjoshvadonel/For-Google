def numIslands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(r, c):
        # stop if out of bounds or water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return

        grid[r][c] = '0'   # sink this land cell (mark visited)

        # explore all 4 directions
        dfs(r+1, c)   # down
        dfs(r-1, c)   # up
        dfs(r, c+1)   # right
        dfs(r, c-1)   # left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':   # found new island
                count += 1
                dfs(r, c)           # sink entire island

    return count

# Test
grid1 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(numIslands(grid1))  # 3

grid2 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
print(numIslands(grid2))  # 1