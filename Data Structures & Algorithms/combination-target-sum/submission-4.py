class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, total, subset):
            if total > target:
                return
            if i >= len(nums):
                return
            if total == target:
                res.append(subset[::])
                return
            
            subset.append(nums[i])
            dfs(i, total + nums[i], subset) # add the same number
            
            subset.pop()
            dfs(i+1, total, subset) # skip the number
            
        dfs(0, 0, [])
        return res