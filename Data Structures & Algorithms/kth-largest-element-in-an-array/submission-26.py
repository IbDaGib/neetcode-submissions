import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        l, r = 0, len(nums)-1
        def quick(l,r):
            pivot_idx = random.randint(l,r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p > k:
                return quick(l, p - 1)
            elif p < k:
                return quick(p + 1, r)
            else:
                return nums[p]

            

        return quick(l,r)
