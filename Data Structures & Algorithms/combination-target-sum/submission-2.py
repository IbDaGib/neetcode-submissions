class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # subset = []

        def dfs(i, subset, total):
            if i == len(nums):
                return
            elif total == target:
                res.append(subset[::])
                return
            elif total > target:
                return

            # try current number again
            subset.append(nums[i])
            total += nums[i]
            dfs(i, subset, total)

            # keep current number try next number
         
            # dfs(i+1, subset)

            # remove current number try next number
            subset.pop()
            total -= nums[i]
            dfs(i+1, subset, total)



        dfs(0, [], 0)
        return res