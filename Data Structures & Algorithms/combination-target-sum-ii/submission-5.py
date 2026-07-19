class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, total, sublist):
            if total == target:
                res.append(sublist[::])
                return
            if i >= len(candidates) or total > target:
                return
            
            sublist.append(candidates[i])
            dfs(i+1, total + candidates[i], sublist)
            sublist.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total, sublist)


        dfs(0,0,[])
        return res