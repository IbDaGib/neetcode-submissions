class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                target = a + nums[l] + nums[r]
            
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    r -= 1
            
        return res


    #-4,-1,-1,0,1,2
    # a  j
