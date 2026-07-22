class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, sublist):
            if len(nums) == 0:
                res.append(sublist[::])
                return
            for i in range(len(nums)):
                sublist.append(nums[i])
                dfs(nums[:i] + nums[i+1:] , sublist)
                sublist.pop()

        dfs(nums, [])
        return res