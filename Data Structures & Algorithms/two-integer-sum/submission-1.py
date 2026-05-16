class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for n in nums: # helps cut things out
        #     if n > target:
        #         nums.remove(n)
        # hashmap solution
        # Time = O(n)
        # Space = O(n)
        hash = {}
        for i, n in enumerate(nums):
            y = target - n
            if y in hash:
                return [hash[y], i]
            hash[n] = i
        
        
        
        
            

        