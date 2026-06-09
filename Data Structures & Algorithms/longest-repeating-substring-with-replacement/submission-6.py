class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        res = 0
        hashS = defaultdict(int)
        l = 0
        for r in range(len(s)):
            hashS[s[r]] += 1
            maxf = max(maxf, hashS[s[r]])
            if (r-l + 1) - maxf > k:
                hashS[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res






