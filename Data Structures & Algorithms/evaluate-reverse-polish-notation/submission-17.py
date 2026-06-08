class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            i = tokens.pop()
            if i not in "+-/*":
                return int(i)

            right = dfs()
            left = dfs()

            if i == '+':
                return left + right
            elif i == '-':
                return left - right
            elif i == '*':
                return left * right
            elif i == '/':
                return int(left / right)

        return dfs()
        