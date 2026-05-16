class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for n in nums:
            res[n] = res.get(n, 0) + 1

        heap = []
        for n in res.keys():
            heapq.heappush(heap, (res[n], n))
            if len(heap) > k:
                heapq.heappop(heap)

        sol = []
        for i in range(k):
            sol.append(heapq.heappop(heap)[1])
        return sol


       