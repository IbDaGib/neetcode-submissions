class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        k = len(nums) - k
        for i in nums:
            heapq.heappush_max(heap, i)
        
        while len(heap) > k+1:
            heapq.heappop_max(heap)

        return heap[0]