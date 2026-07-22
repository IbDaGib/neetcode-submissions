class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        res = []
        def dfs(i, total, sublist):
            if total == target:
                res.append(sublist[::])
                return
            if total > target or i == len(nums):
                return
          
            sublist.append(nums[i])
            dfs(i+1, total+nums[i], sublist)
            sublist.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, total, sublist)

        dfs(0,0,[])
        return res