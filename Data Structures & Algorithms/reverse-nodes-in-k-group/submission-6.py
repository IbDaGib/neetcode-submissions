# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        groupPrev = dummy
        while True:
            kth = self.getkth(groupPrev, k)
            if not kth: # no more groups to reverse
                break
            groupNext = kth.next
            start = groupPrev.next
            prev = kth.next
            while start != groupNext: # stops before next group
                tmp = start.next
                start.next = prev
                prev = start
                start = tmp

            # prepares for next cycle to handle next group
            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp
        return dummy.next
    
    def getkth(self, node, k):
        while node and k > 0:
            k -= 1
            node = node.next
        return node