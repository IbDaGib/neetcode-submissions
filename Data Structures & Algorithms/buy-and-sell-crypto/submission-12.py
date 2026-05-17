class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        r = 1
        l = 0
        while r < len(prices):
            while prices[l] > prices[r]:
                l += 1
            res = max(res, prices[r] - prices[l])
            r += 1

        return res


        # 10, 1, 5, 6, 7, 1
        #     l        