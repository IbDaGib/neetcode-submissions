import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums)-1
        k = len(nums) - k
        def quick(l,r):
            if l > r:
                return
            p_idx = random.randint(l,r)
            nums[p_idx], nums[r] = nums[r], nums[p_idx]
            p = l
            pivot = nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p > k: return quick(l, p-1)
            elif p < k: return quick(p+1, r)
            else: return nums[p]

        return quick(l,r)