class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            heapq.heappush(maxHeap, [-dist, x, y])  # Store negative distance for max-heap

            if len(maxHeap) > k:  # Maintain only k closest points
                heapq.heappop(maxHeap)  # Remove the farthest point

        res = [[x, y] for _, x, y in maxHeap]  # Extract results
        return res