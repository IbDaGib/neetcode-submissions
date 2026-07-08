class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        for i in count:
            buckets[count[i]].append(i)

        for i in reversed(buckets):
            for j in i:
                if len(res) == k:
                    return res
                res.append(j)
        return res


