class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x-y != 0:
                heapq.heappush(heap, (x-y))
        return 0 if len(heap) == 0 else abs(heap[0])