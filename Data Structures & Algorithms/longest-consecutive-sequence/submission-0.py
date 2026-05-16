class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)

        for i in nums:
            if i-1 not in nums:
                length = 1
                while (i + length) in nums:
                    length += 1
                longest = max(length, longest)
        
        return longest

    # O(n) time cuz each element is only processed once! think about it
    # 3,4,5 are only processed once because they have i-1
    # 2, 10, 20 are only processed they don't have i-1