# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # second half of list
        slow.next = None
        prev = None

        while second: # reverses second portion of list
            temp = second.next
            second.next = prev # reverse -> to <-
            prev = second 
            second = temp # moves second forward


        # merge two halfs
        first, second = head, prev
        
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


        
