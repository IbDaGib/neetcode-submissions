# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        a = head
        b = head.next
        while b and b.next:
            a = a.next
            b = b.next.next

        prev = None
        c = a.next
        a.next = None

        while c:
            tmp = c.next
            c.next = prev
            prev = c
            c = tmp
        
        d, c = head, prev
        while c:
            tmp1, tmp2 = d.next, c.next
            d.next = c
            c.next = tmp1
            d, c = tmp1, tmp2