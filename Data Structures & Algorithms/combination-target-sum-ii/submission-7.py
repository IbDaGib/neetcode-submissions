class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        res = []
        def dfs(i, total, sublist):
            if total == target:
                res.append(sublist[::])
                return
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if total + nums[j] > target:
                    break
                sublist.append(nums[j])
                dfs(j + 1, total + nums[j], sublist)
                sublist.pop()


        dfs(0,0,[])
        return res