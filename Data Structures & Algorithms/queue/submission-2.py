class Node:
    def __init__(self, val, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self) -> None:
        self.left = Node(-1)
        self.right = Node(-1)
        self.left.next = self.right
        self.right.prev = self.left

    def isEmpty(self) -> bool:
        return self.left.next == self.right
    
    def append(self, val:int) -> None:
        newNode = Node(val)
        prev, next = self.right.prev, self.right

        newNode.next = next
        newNode.prev = prev
        prev.next = newNode
        next.prev = newNode

    def appendleft(self, val:int) -> None:
        newNode = Node(val)
        prev, next = self.left, self.left.next

        newNode.next = next
        newNode.prev = prev
        prev.next = newNode
        next.prev = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        targetNode = self.right.prev
        val = targetNode.val
        prev, next = targetNode.prev, self.right

        prev.next = next
        next.prev = prev

        return val
    
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        targetNode = self.left.next
        val = targetNode.val
        prev, next = self.left, targetNode.next

        prev.next = next
        next.prev = prev

        return val
    