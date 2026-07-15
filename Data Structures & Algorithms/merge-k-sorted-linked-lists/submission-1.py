# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
      
        while len(lists) > 1:
            l1, l2 = lists.pop(), lists.pop()
            lists.append(self.merge(l1, l2))

        return lists[0]

    
    def merge(self, l1, l2) -> Optional[ListNode]:
        cur = ListNode()
        dummy = cur
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        
        return dummy.next
