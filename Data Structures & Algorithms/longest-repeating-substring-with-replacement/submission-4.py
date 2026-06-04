class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        hash = defaultdict(int)
        maxf = 0
        for r in range(len(s)):
            hash[s[r]] += 1
            maxf = max(maxf, hash[s[r]])

            if (r-l+1) - maxf > k:
                hash[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)

        return res

                