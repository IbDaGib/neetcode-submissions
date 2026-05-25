class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] * _ for _ in range(len(nums)+1)]
        count = Counter(nums)

        for i in count:
            bucket[count[i]].append(i)

        res = []
        for i in reversed(bucket):
            for j in i:
                if len(res) == k:
                    return res
                res.append(j)

        return res
            