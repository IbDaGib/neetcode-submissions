class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for n in nums:
            res[n] = res.get(n, 0) + 1

        return heapq.nlargest(k, res.keys(), key=res.get)


       