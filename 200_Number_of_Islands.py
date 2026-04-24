class Solution:
    def numIslands(self, grid):
        row, cols = len(grid), len(grid[0])
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        islands = 0

        def inbound(r, c):
            return 0 <= r < row and 0 <= c < cols

        def dfs(row, col):
            grid[row][col] = "0"

            for row_change, col_change in direction:   # fixed typo
                new_row, new_col = row + row_change, col + col_change
                if inbound(new_row, new_col) and grid[new_row][new_col] == "1":
                    dfs(new_row, new_col)
            
        for rows in range(row):
            for col in range(cols):
                if grid[rows][col] == "1":
                    islands += 1  
                    dfs(rows, col)

        return islands
