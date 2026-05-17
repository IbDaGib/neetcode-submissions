class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0,9):
            hash_row = set()
            for j in range(0,9):
                if board[i][j] in hash_row and board[i][j] != '.':
                    return False
                hash_row.add(board[i][j])

        for i in range(0,9):
            hash_col = set()
            for j in range(0,9):
                if board[j][i] in hash_col and board[j][i] != '.':
                    return False
                hash_col.add(board[j][i])

        for square in range(0,9):
            hash_sq = set()
            for i in range(0,3):
                for j in range(0,3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] in hash_sq and board[row][col] != '.':
                        return False
                    hash_sq.add(board[row][col])

        return True
        
        
                
