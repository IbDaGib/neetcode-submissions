class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1
            while l < r:
                target = nums[l] + nums[r] + a
                if target < 0:
                    l += 1
                elif target > 0:
                    r -= 1
                else:
                    res.append([nums[l],nums[r],a])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    r -= 1

        return res
