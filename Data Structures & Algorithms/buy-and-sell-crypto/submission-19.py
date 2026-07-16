class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(1, len(prices)):
            while prices[l] > prices[r]:
                l = r
            res = max(res, (prices[r]-prices[l]))

        return res