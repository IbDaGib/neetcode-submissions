class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        moves = [[0,1], [0,-1], [1,0], [-1,0]]
        q = deque()
        fresh = 0
        time = 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while fresh > 0 and q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc, in moves:
                    row, col = r+dr, c+dc
                    if (r+dr in range(ROWS) and c+dc in range(COLS) and grid[r+dr][c+dc] == 1):
                        grid[r+dr][c+dc] = 2
                        q.append((r+dr, c+dc))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
            


