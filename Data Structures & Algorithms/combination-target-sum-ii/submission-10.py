class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(candidates)
        def dfs(i, total, sub):
            if total == target:
                res.append(sub[::])
                return
            if i+1 > len(nums):
                return

            for j in range(i, len(nums)):
                if j>i and nums[j] == nums[j-1]:
                    continue
                if nums[j] + total > target:
                    return
                sub.append(nums[j])
                dfs(j+1, total + nums[j], sub)
                sub.pop()


        dfs(0,0,[])
        return res