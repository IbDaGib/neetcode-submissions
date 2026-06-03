class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for i in operations:
            if i == '+':
                a,b = int(stack[-1]), int(stack[-2])
                stack.append(a+b)
                res += a+b
            elif i == "C":
                res -= stack.pop()
            elif i == "D":
                a = int(stack[-1])
                stack.append(2*a)
                res += (2*a)
            else:
                stack.append(int(i))
                res += int(i)

        return res