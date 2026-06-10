class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse=True)

        for p, s in cars:
            steps = (target-p) / s
            if not stack or steps > stack[-1]:
                stack.append(steps)

        return len(stack)