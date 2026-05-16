class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r,c):
            if (r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0 or (r,c) in visit):
                return 0 
            visit.add((r,c))
            cnt = 1
            for dr, dc in directions:
                cnt += dfs(r + dr, c + dc)

            return cnt
        
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c))
        
        return maxArea


        