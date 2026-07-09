class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l, r = 0, 0
        res = []
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res

# 1210426
# q = 0, l = 0, r = 0
# q = 1, l = 0, r = 1
# q = 12, l = 1, r = 2, res = 2
# q = 123, l = 2, r = 3, res = 2