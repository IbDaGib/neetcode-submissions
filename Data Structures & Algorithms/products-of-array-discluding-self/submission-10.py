class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in reversed(range(len(nums))):
            res[i] *= postfix
            postfix *= nums[i]

        return res

        # 1,2,4,6
        # prefix = 1
        # res = 1,1,1,1
        # prefix = 1
        # res = 1,1,1,1
        # prefix = 2
        # res = 1,1,2,1
        # prefix = 8
        # res = 1,1,2,8

        