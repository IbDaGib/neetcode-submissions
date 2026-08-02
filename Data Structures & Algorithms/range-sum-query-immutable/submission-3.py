class NumArray:

    def __init__(self, nums: List[int]):
        self.res = [0] * len(nums)
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            self.res[i] = prefix

    def sumRange(self, left: int, right: int) -> int:
        right = self.res[right]
        left = self.res[left-1] if left > 0 else 0
        return right - left
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)