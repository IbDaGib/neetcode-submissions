# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head # pointer 1
        prev = None # pointer 2

        while curr:
            nxt = curr.next # tmp to iterate
            curr.next = prev
            prev = curr  # iterate pointer 2
            curr = nxt # iterate pointer 1

        return prev