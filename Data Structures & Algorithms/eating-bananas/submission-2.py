class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = max(piles)
        while l <= r:
            m = (r+l) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(float(i/m))
            if hours <= h:
                r = m - 1
                k = min(k, m)
            else:
                l = m + 1
        
        return k
