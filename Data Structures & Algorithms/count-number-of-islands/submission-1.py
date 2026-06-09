class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(i,j):
            if (i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == '0'):
                return
            
            grid[i][j] = '0'
            for di, dj in directions:
                dfs(i + di, j + dj)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res += 1
        return res