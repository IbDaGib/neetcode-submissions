class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, n in enumerate(nums): # i is index, n is number
            diff = target - n
            if diff in hash:
                return [hash[diff], i]
            hash[n] = i
            

        
        
        
        
            

        