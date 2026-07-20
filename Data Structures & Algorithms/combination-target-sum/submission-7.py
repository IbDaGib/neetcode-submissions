class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, total, sublist):
            if total == target:
                res.append(sublist[::])
                return
            if total > target or i > len(nums)-1:
                return
            
            sublist.append(nums[i])
            dfs(i, total + nums[i], sublist)
            # dfs(i+1, total + nums[i], sublist)

            sublist.pop()
            dfs(i+1, total, sublist)
            # dfs(i+1, total + nums[i], sublist)

        dfs(0,0,[])
        return res