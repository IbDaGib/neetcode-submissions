class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.minimum.append(val)
        else:
            self.stack.append(val)
            if val <= self.minimum[-1]:
                self.minimum.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.minimum[-1]:
            self.minimum.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minimum[-1]:
            return self.minimum[-1]
        else:
            return 0
        
