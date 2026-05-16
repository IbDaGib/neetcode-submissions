class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for n in nums:
            if n in res:
                res[n] += 1
            else:
                res[n] = 1

       
        print(heapq.nlargest(k, res.keys(), key=res.get))
        return heapq.nlargest(k, res.keys(), key=res.get)


       