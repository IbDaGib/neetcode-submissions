class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 12345 k = 3
        # [123]45
        # 1[234]5
        # 12[345]

        res = []
        l = 0
        # maxi = max(nums[l:k]) # initiate max
        # res.append(maxi)
        window = Counter(nums[l:k]) # initiate window
        for r in range(k-1, len(nums)):
            maxi = max(nums[l:r+1])
            res.append(maxi)
            # print(nums[l:r+1], l, r)
            window[nums[r]] += 1
            window[nums[l]] -= 1
            l += 1

        return res
