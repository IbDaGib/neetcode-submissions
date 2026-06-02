class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for i in nums:
            if i-1 in nums:
                continue
            tmp = 0
            while i in nums:
                i += 1
                tmp += 1
            res = max(res, tmp)

        return res