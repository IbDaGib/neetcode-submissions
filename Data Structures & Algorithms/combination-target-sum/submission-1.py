class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # subset = []

        def dfs(i, subset):
            if i == len(nums):
                return
            elif sum(subset) == target:
                res.append(subset[::])
                return
            elif sum(subset) > target:
                return

            # try current number again
            subset.append(nums[i])
            dfs(i, subset)

            # keep current number try next number
         
            # dfs(i+1, subset)

            # remove current number try next number
            subset.pop()
            dfs(i+1, subset)



        dfs(0, [])
        return res