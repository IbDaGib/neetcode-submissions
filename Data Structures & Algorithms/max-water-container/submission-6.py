class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) -1
        res = 0
        # consider width * min height
        # cant sort
        # find max height and max length
        while l < r:
            cur = min(heights[l], heights[r]) * (r-l)
            res = max(res, cur)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return res