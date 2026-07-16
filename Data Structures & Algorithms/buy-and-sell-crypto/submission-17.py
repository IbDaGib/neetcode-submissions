class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        # r = 1
        for r in range(1, len(prices)):
            while l < r and prices[l] > prices[r]:
                l = r
            res = max(res, (prices[r]-prices[l]))
        

        return res