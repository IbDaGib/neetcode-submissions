class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # create freq arr
        freq = [[] for i in range(len(nums) + 1)]
        
        # create the hashmap
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # add to freq arr
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in reversed(range(1, len(freq))): # start with num that occur most freq
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
