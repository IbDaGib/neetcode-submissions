"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache = {}
        cache[None] = None

        cur = head
        while cur: # create all new nodes
            copy = Node(cur.val)
            cache[cur] = copy
            cur = cur.next

        cur = head
        while cur: # map new nodes
            copy = cache[cur]
            copy.next = cache[cur.next]
            copy.random = cache[cur.random]
            cur = cur.next

        return cache[head]