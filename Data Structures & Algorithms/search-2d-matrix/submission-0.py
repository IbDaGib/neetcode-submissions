class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # solution  = target * len(matrix)
        res = 0
        for i in matrix:
            res = self.binarySearch(i, target)
            if res == target:
                return True

        return False


    def binarySearch(self, arr: List[int], target: int) -> int:
        L, R = 0, len(arr)-1

        if arr[L] > target:
            return -1
        if arr[R] < target:
            return -1

        while L <= R:
            mid = L + ((R-L) // 2)
            if arr[mid] < target:
                L = mid + 1
            elif arr[mid] > target:
                R = mid - 1
            else:
                return arr[mid]
        return -1

        