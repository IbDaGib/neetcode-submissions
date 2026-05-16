class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        visit = set((0,0))
        queue = deque([(0,0)])
        length = 0

        def bfs(r, c):
            moves = [[0,1], [0, -1], [1,0], [-1,0]]
            for dr, dc in moves:
                if (min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS or (r+dr, c+dc) in visit or grid[r+dr][c+dc] == 1):
                    continue
                queue.append((r+dr, c+dc))
                visit.add((r+dr, c+dc))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                bfs(r,c)
            length += 1
        return -1
                
                