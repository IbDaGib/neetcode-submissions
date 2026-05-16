class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            hash[i] = hash.get(i, 0) + 1

        arr = []
        for num, cnt in hash.items():
            arr.append([cnt, num])
        
        arr.sort()
        res = []

        while len(res) < k:
            res.append(arr.pop()[1])

        return res


       