class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0
        nums = set(nums)

        for i in nums:
            if i-1 in nums:
                continue
            tmp = 1
            j = i
            while j+1 in nums:
                tmp += 1
                j += 1
            res = max(res, tmp)

        return res