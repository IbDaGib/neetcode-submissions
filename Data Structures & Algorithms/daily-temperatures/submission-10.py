class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][1]:
                index, temp = stack.pop()
                res[index] = i-index
            
            stack.append((i,t))

        return res

# 30,38,30,36,35,40,28
# stack = ((0,30), )
# 38 > 30: True, index = 0, temp = 30, res[0] = 1-0 = 1