class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if len(stack) > 0:
                    if c == ')' and stack[-1] != '(':
                        return False 
                    elif c == ']' and stack[-1] != '[':
                        return False 
                    elif c == '}' and stack[-1] != '{':
                        return False 
                else:
                    return False
            
                stack.pop()
        
        return len(stack) == 0