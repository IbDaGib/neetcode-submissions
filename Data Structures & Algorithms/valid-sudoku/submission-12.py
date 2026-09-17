class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        cols = defaultdict(list)
        rows = defaultdict(list)
        sq = defaultdict(list)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == '.':
                    continue
                elif (board[i][j] in rows[i] or board[i][j] in cols[j] or
                board[i][j] in sq[(i//3,j//3)]):
                    return False
                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                sq[(i//3,j//3)].append(board[i][j]) 
        return True
