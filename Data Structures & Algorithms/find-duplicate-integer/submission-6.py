class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0] # Start slow at head.next
        fast = nums[nums[0]]  # Start fast at head.next.next

        # Find an intersection point inside the cycle.
        while slow != fast:
            slow = nums[slow] # slow.next
            fast = nums[nums[fast]] # fast.next.next

        slow2 = 0 # Start another pointer at the head.
        # Move both one step at a time until they meet.
        # The meeting point is the entrance to the cycle (the duplicate).
        while slow != slow2:
            slow = nums[slow] # slow.next
            slow2 = nums[slow2] # slow2.next

        return slow