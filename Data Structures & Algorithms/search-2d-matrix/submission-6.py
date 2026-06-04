class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first find row
        # then find target in row
        # 2 loops
        l = 0
        r = len(matrix)-1

        while l <= r:
            row = (r + l) // 2
            if target > matrix[row][-1]:
                l = row + 1
            elif target < matrix[row][0]:
                r = row - 1
            else:
                break

        if l > r:
            return False

        l = 0
        r = len(matrix[row])-1
        while l <= r:
            m = (r+l) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True

        return False

