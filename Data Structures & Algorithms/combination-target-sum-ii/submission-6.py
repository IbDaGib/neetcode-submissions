class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nums = candidates
        nums.sort()
        def dfs(i, total, sublist):
            if total == target:
                res.append(sublist[::])
                return
            if total > target or i > len(nums)-1:
                return
            
            # sublist.append(nums[i])
            # dfs(i+1, total + nums[i], sublist)
            # sublist.pop()
            # while i + 1 < len(nums) and nums[i] == nums[i+1]:
            #     i += 1
            # dfs(i+1, total, sublist)

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                if total + nums[j] > target:
                    break
                sublist.append(nums[j])
                dfs(j+1, total + nums[j], sublist)
                sublist.pop()

        dfs(0,0,[])
        return res