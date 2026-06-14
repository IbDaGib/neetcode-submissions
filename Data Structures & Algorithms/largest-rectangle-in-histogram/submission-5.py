class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                start = index
                res = max(res, height * (i - index))

            stack.append((start,h))

        for i, h in stack:
            res = max(res, h * (len(heights)-i))

        return res