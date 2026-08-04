class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heap = [-s for s in stones] # maxheap
        heapq.heapify(heap)
        print(heap)
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            print(heap)
            print(x,y)
            if x == y:
                continue
            else:
                heapq.heappush(heap, (x-y))
        return 0 if len(heap) == 0 else abs(heap[0])