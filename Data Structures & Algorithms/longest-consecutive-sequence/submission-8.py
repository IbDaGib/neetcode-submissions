class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)

        for i in nums:
            if (i-1) not in nums:
                tmp = 1
                while(i + tmp) in nums:
                    tmp += 1
                res = max(res, tmp)

        return res


