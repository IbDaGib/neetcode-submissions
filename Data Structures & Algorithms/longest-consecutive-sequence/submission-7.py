class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        res = 1

        count = Counter(nums)
        for i in count:
            tmp = 1
            j = i+1
            while j in count:
                tmp += 1
                j += 1
            res = max(tmp, res)

        return res


