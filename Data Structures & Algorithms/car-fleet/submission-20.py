class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sp = sorted(zip(position, speed), reverse=True)
        # print(sp)
        stack = []
        for p, s in sp:
            steps = (target - p) / s
            if stack and steps <= stack[-1]:
                continue
            stack.append(steps)
            
        return len(stack)