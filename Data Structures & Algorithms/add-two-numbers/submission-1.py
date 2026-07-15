# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""

        while l1:
            str1 += "".join(str(l1.val))
            l1 = l1.next

        while l2:
            str2 += "".join(str(l2.val))
            l2 = l2.next

        res = int(str1[::-1]) + int(str2[::-1])

        dummy = ListNode()
        cur = dummy

        # The answer must also be stored in reverse order.
        for digit in str(res)[::-1]:
            cur.next = ListNode(int(digit))
            cur = cur.next

        return dummy.next