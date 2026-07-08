class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        hashS = defaultdict(int)
        maxf = 0
        for r in range(len(s)):
            hashS[s[r]] += 1
            maxf = max(maxf, hashS[s[r]])
            while (r-l+1) - maxf > k:
                hashS[s[l]] -= 1
                l += 1
            res = max(r-l+1, res)
    
            

        return res
