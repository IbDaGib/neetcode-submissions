# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while groupPrev:
            kth = self.getkth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            start = groupPrev.next
            prev = kth.next
            while start != groupNext:
                tmp = start.next
                start.next = prev
                prev = start
                start = tmp

            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp
        return dummy.next    
    
    def getkth(self, node, k):
        while node and k > 0:
            k -= 1
            node = node.next
        return node