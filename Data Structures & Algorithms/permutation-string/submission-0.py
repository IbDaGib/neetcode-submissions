class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        for r in range(len(s1), len(s2)+1):
            print(s2[l:r])
            if sorted(s2[l:r]) == sorted(s1):
                return True
            l+=1

        return False