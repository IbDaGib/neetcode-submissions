class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        arr = [0] * 26
        arr2 = [0] * 26
        for i in range(len(s1)):
            arr[ord(s1[i]) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1
        if arr2 == arr:
            return True
            
        l = 0
        for r in range(len(s1), len(s2)):
            arr2[ord(s2[r]) - ord('a')] += 1
            arr2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if arr2 == arr:
                return True
        
        return False
        # if len(s1) > len(s2):
        #     return False
        # hash1 = Counter(s1)
        # hash2 = Counter(s2[:len(s1)])
        # if hash1 == hash2:
        #     return True
        # l = 0
        # for r in range(len(s1), len(s2)):
        #     hash2[s2[r]] += 1
        #     hash2[s2[l]] -= 1
        #     l+=1
        #     if hash1 == hash2:
        #         return True
        # return False

