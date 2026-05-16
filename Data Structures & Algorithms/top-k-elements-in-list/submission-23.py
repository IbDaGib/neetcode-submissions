class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for _ in range(len(nums)+1)]
        hash = {}

        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        
        for i in hash:
            res[hash[i]].append(i)
        print(res)

        final = []
        for i in reversed(res):
            for n in i: 
                if len(final) == k:
                    return final
                final.append(n)

        return final

        