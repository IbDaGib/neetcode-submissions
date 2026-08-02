class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cursum = 0
        prefixsums = defaultdict(int)
        prefixsums[0] = 1
        for num in nums:
            cursum += num
            diff = cursum - k
            res += prefixsums[diff]
            prefixsums[cursum] += 1
        return res