class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = float('inf')
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                mini = min(mini, nums[m])
                r = m - 1
        

        return mini