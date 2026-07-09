class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {')' : '(', ']' : '[', '}' : '{'}
        for i in s:
            if i not in dict:
                stack.append(i)
            else:
                if stack and dict[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        

        return len(stack) == 0