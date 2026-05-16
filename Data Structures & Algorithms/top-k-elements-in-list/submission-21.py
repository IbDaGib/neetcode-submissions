class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            hash[i] += 1

        for i, n in hash.items():
            freq[n].append(i)
        
        res = []
        for i in reversed(freq):
            # if len(res) != k:
            print(i)
            for n in i:
                res.append(n)
                if len(res) == k:
                    return res
