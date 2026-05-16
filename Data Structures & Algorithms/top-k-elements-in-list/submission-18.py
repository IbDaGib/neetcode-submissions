class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)
        
        for i, n in count.items():
            freq[n].append(i) 
        
        print(freq)
        res = []
        
        for i in reversed(freq):
            if i:
                for c in i:
                    if len(res) < k:
                        res.append(c)
                    else:
                        return res
        return res
