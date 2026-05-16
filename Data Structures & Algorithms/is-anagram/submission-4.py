class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first case
        if len(s) != len(t):
            return False
        
        hash = {}
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1

        for i in t:
            if i in hash and hash[i] > 0:
                hash[i] -= 1
            else:
                return False
        
        return True
        
        