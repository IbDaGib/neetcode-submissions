class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        while l < r:
            if lmax <= rmax:
                # res += lmax - height[l]
                l += 1
                lmax = max(lmax, height[l])
                # l += 1
                res += lmax - height[l]
            else:
                # res += rmax - height[r]
                r -= 1
                rmax = max(rmax, height[r])
                # r -= 1
                res += rmax - height[r]
        return res