class DynamicArray:
    
    def __init__(self, capacity: int):
        self.a = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        if i >= self.size:
            return -1
            
        return self.a[i]

    def set(self, i: int, n: int) -> None:
        if i >= self.size:
            return -1
        
        self.a[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            # if no space
            self.resize()
        
        self.a[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # soft delete
        self.size -= 1
        return self.a[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        new_a = [0] * self.capacity

        for i in range(self.size):
            new_a[i] = self.a[i]

        self.a = new_a

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity