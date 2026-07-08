class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        maxA = 0

        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                maxA += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                maxA += maxR - height[r]

        return maxA

