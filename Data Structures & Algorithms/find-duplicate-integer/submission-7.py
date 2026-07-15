class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0] # head.next
        fast = nums[nums[0]] # head.next.next

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow