class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums)+1)]
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        # print(arr)
        for n, cnt in count.items():
            arr[cnt].append(n)

        res = []
        for i in reversed(range(len(arr))):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res
            