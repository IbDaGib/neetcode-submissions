class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # countT = Counter(s)
        window = defaultdict(int)
        l = 0
        freq = 0
        for r in range(len(s)):
            window[s[r]] += 1
            freq = max(freq, window[s[r]])
            while (r-l+1) - freq > k:
                window[s[l]] -= 1
                l += 1
        return r-l+1
        
