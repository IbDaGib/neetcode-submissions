class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            prefix[i] += pre
        
        post = 0
        for i in reversed(range(len(nums))):
            post += nums[i]
            postfix[i] += post

        for i in range(len(nums)):
            if postfix[i] == prefix[i]:
                return i
        
        return -1