class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1,2,4,6
        # 1,2,4,6
        # Prefix, postfix
        # 1,2,8,24
        # 6,24,8,2
        # 1,2,8,24
        arr = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            arr[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in reversed(range(len(nums))):
            arr[i] *= postfix
            postfix *= nums[i]
        
        return arr
