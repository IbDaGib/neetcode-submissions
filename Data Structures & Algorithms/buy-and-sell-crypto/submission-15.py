class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        r = 0
        while r < len(prices):
            if prices[l] <= prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
                r += 1
            else:
                l = r

        return maxP

    # 10,1,5,6,7,1
    #    l
    #      r

    # 7,1,5,3,6,4
    #   l
    #         r