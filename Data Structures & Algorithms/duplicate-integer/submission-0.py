class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hashset solution 
        # time = O(n)
        # space = O(n)
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

        # sort solution
        # time = O(nlogn)
        # space = O(1) 
        # nums = sorted(nums)
        # print(nums)
        # for i in range(len(nums) - 1): 
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False