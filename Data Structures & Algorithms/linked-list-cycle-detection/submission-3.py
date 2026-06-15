# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        curr = head.next
        prev = head

        while curr and curr.next:
            if curr == prev:
                return True
            curr = curr.next.next
            prev = prev.next

        return False