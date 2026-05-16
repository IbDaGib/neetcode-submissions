class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)
        
        for i, n in count.items():
            freq[n].append(i) 
        
        res = []
        for i in reversed(freq):
            if i:
                for n in i:
                    res.append(n)
                    if len(res) == k:
                        return res
