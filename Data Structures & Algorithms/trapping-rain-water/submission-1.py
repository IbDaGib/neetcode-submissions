class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        
        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])
            if lmax < rmax:
                area = lmax - height[l]
                res += area
                l += 1
            else:
                area = rmax - height[r]
                res += area
                r -= 1

        return res

        
    # 0203101321
    # 020
    # LL
    # lll
    # area = 2 * 