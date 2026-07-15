class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i, subset):
            if i+1 > len(nums):
                res.append(subset[::])
                return

            subset.append(nums[i])
            dfs(i+1, subset)

            subset.pop()
            dfs(i+1, subset)


        dfs(0, [])
        return res