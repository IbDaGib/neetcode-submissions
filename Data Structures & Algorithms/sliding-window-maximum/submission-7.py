class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        maxi = max(nums[l:k]) # initiate max
        window = Counter(nums[l:k]) # initiate window
        for r in range(k-1, len(nums)):
            window[nums[r]] += 1
            window[nums[l]] -= 1
            maxi = max(nums[l:r+1])
            res.append(maxi)
            l += 1

        return res
