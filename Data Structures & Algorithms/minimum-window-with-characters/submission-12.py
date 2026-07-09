class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        window = defaultdict(int)
        have = 0
        need = len(countT)
        l = 0
        i, j = -1, -1
        resLen = float('inf')
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    i, j = l, r
                window[s[l]] -= 1
                if window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        return s[i:j+1] if resLen != float('inf') else ""
