class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS1 = Counter(s1)
        countS2 = Counter(s2[0:len(s1)])

        l = 0
        for r in range(len(s1), len(s2)):
            if countS1 == countS2:
                return True
            
            countS2[s2[r]] += 1
            countS2[s2[l]] -= 1
            
            if countS2[s2[l]] == 0:
                del countS2[s2[l]]
            l+=1
        
        return countS1 == countS2