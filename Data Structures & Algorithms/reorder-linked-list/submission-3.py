# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        p1, p2 = head, head

        while p2 and p2.next:
            p2 = p2.next.next
            p1 = p1.next

        p3 = p1.next
        p1.next = None # Split the list into two halves
        prev = None

        while p3: # reverse second half of list
            tmp = p3.next
            p3.next = prev
            prev = p3
            p3 = tmp
        
        p4 = head
        p5 = prev

        while p5:
            tmp = p4.next
            tmp2 = p5.next
            p4.next = p5
            p5.next = tmp
            p4 = tmp
            p5 = tmp2
