class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i not in "+CD":
                stack.append(int(i))
                continue
            else:
                if i == '+':
                    a,b = int(stack[-1]), int(stack[-2])
                    stack.append(a+b)
                elif i == "C":
                    stack.pop()
                elif i == "D":
                    a = int(stack[-1])
                    stack.append(a*2)
            print(stack)

        return sum(stack)