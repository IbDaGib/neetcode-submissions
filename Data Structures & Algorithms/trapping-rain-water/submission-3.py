class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]

        maxArea = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                maxArea += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                maxArea += maxR - height[r]

        return maxArea