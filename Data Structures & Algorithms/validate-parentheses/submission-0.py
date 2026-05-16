class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Dict = {")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c not in Dict:
                stack.append(c)
                continue
            if not stack or stack[-1] != Dict[c]:
                return False
            stack.pop()
        
        return not stack
        