class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(candidates)
        def dfs(i, total, sub):
            if total == target:
                res.append(sub[::])
                return
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                if nums[j] + total > target:
                    return
                sub.append(nums[j])
                dfs(j+1, total + nums[j], sub)
                sub.pop()

        dfs(0,0,[])
        return res

        # res = []
        # nums = sorted(candidates)
        # def dfs(i, total, sub):
        #     if total == target:
        #         res.append(sub[::])
        #         return
        #     if total > target:
        #         return
        #     if i+1 > len(nums):
        #         return

        #     while i + 1 < len(nums):
        #         if nums[i] == nums[i+1]:
        #             i += 1
        #     sub.append(nums[i])
        #     dfs(i+1, total + nums[i], sub)
        #     sub.pop()
        #     dfs(i+1, total, sub)
        
        
        # dfs(0,0,[])
        # return res