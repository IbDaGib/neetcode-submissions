class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack = [tokens[0]]

        # while stack:
        #     n = stack.pop()
        #     if n 
        stack = []
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            else:
                a, b = stack.pop(), stack.pop()
                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(b-a)
                elif i == '*':
                    stack.append(a*b)
                elif i == '/':
                    stack.append(int(float(b/a)))

        return stack[-1]
        