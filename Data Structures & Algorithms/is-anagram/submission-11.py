class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = defaultdict(int)
        for i in s:
            hash_s[i] += 1

        hash_t = defaultdict(int)
        for i in t:
            hash_t[i] += 1

        return hash_s == hash_t


