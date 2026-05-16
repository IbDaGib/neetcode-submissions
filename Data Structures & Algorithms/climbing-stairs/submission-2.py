class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        n1, n2 = 1, 1
        for i in range(2, n+1):
            temp = n2
            n2 = n1 + n2
            n1 = temp
        
        return n2
        