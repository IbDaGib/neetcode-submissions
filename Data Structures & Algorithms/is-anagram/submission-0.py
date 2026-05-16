class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first case
        if len(s) != len(t):
            return False

        # sort method
        # time = O(nlogn)
        # Space = O(1)
        # return sorted(s) == sorted(t)
        # in python you can just check if 2 strings are the same by doing ==

        # Hashmap solution 
        # Time = O(n) or O(s+t)
        # Space = O(n) or O(s+t)
        count_s, count_t = {}, {}

        for i in range(len(s)):
            # filling up the hashmaps
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        for x in count_s:
            if count_s[x] != count_t.get(x, 0):
                return False

        return True
        