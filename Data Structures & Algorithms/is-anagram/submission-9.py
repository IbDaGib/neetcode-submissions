class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        for i in s:
            hash_s[i] = hash_s.get(i, 0) + 1
        
        hash_t = {}
        for i in t:
            hash_t[i] = hash_t.get(i, 0) + 1

        return hash_s == hash_t