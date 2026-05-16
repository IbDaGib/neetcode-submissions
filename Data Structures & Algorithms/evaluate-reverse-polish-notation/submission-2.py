class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])

        sum = 0
        for i in tokens:
            if i == '+':
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                sum = int(n1 + n2)
                stack.append(sum)
            elif i == '-':
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                sum = int(n1 - n2)
                stack.append(sum)
            elif i == '*':
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                sum = int(n1 * n2)
                stack.append(sum)
            elif i == '/':
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                sum = int(n1 / n2)
                stack.append(sum)
            else: 
                stack.append(i)

        return stack[-1]
        