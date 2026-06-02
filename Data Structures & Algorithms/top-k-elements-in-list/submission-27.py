class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]
        res = []
        for i in count:
            freq[count[i]].append(i)

        for i in reversed(freq):
            for n in i:
                res.append(n)
                if len(res) == k:
                    return res

        