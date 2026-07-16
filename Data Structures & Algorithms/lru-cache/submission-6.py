class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lru  = {}
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.right.prev = self.left
        self.left.next = self.right

    def remove(self, node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev


    def insert(self, node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev


    def get(self, key: int) -> int:
        if key in self.lru:
            self.remove(self.lru[key])
            self.insert(self.lru[key])
            return self.lru[key].val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.remove(self.lru[key])
        self.lru[key] = Node(key, value)
        self.insert(self.lru[key])

        if len(self.lru) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.lru[lru.key]
        
