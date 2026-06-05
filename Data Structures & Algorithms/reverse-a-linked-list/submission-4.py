# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 2 pointers
        curr = head 
        prev = None

        while curr:
            x = curr.next # saving curr.next for iteration
            curr.next = prev # the only op acc happening
            prev = curr # iterating prev pointer
            curr = x # iterating curr pointer

        return prev