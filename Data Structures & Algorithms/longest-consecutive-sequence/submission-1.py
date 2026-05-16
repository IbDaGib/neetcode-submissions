class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = {}
        for n in nums:
            hash[n] = 1 + hash.get(n, 0)

        res = 0
        count = 0
        for i in hash:
            if i-1 not in hash:
                count = 1
                while (i + count) in hash:
                    count += 1
                res = max(res, count)
        return res
    