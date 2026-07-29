class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(candidates)
        def dfs(i, total, subset):
            if total == target:
                res.append(subset[::])
                return
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                if total + nums[j] > target:
                    return
                subset.append(nums[j])
                dfs(j+1, total + nums[j], subset)
                subset.pop()

        dfs(0,0,[])
        return res