class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = (r+l) // 2
            hours = 0
            for i in piles:
                hours += (i + m - 1) // m
            if hours <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        
        return res
