class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)
        def dfs(sub):
            if len(sub) == len(nums):
                res.append(sub[::])
                return
            
            for n in count:
                if count[n] > 0:
                    count[n] -= 1
                    sub.append(n)
                    dfs(sub)
                    count[n] += 1
                    sub.pop()

        dfs([])
        return res