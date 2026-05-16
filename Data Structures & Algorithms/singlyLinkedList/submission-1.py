class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        # dummy node
        self.head = Node(0)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            # if list was empty before inserting
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while i < index and cur:
            # move cur to node before target node
            i += 1
            cur = cur.next

        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True

        return False
        

    def getValues(self) -> List[int]:
        cur = self.head.next # dont wanna include value of dummy node
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next

        return res
         
