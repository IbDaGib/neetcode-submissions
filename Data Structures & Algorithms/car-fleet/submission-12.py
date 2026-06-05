class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = (sorted(zip(position, speed), reverse=True))

        for p, s in cars:
            step = (target-p) / s
            if not stack or step > stack[-1]:
                stack.append(step)



        return len(stack)