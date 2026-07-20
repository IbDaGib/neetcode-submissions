class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, total, sublist):
            if total == target:
                res.append(sublist[::])
                return
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                sublist.append(nums[j])
                dfs(j, total + nums[j], sublist)
                sublist.pop()
        
        dfs(0,0,[])
        return res