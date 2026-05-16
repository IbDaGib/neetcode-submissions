class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = (r-l) * min(heights[l], heights[r])
        
        while l < r:
            run = ((r-l) * min(heights[l], heights[r]))
            res = max(run, res)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res