class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []   # Max heap storing (value, index)
        res = []

        for i in range(len(nums)):
            # Add the current element to the heap.
            heapq.heappush_max(heap, (nums[i], i))

            # Wait until we've formed the first full window.
            if i >= k - 1:

                # Remove elements that are no longer inside the current window.
                # Current window is [i - k + 1, ..., i], so any index <= i - k
                # has fallen out of the window.
                while heap[0][1] <= i - k:
                    heapq.heappop_max(heap)

                # The top of the max heap is the largest element
                # remaining inside the current window.
                res.append(heap[0][0])

        return res