class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = 0 
        r = 1
        count = Counter(nums)
        res = 0

        for i in count:
            if i-1 in count:
                continue
            tmp = 0
            j = i
            while j in count:
                tmp +=1
                j += 1

            res = max(res, tmp)

        return res