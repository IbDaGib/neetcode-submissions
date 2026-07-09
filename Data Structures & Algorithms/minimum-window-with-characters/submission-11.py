class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        hashT = Counter(t)
        window = defaultdict(int)
        have = 0

        l = 0
        i, j = 0,0
        length = float('inf')
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == hashT[s[r]]:
                have += 1

            while have == len(hashT):
                if r-l+1 < length:
                    length = r-l+1
                    i, j = l, r
               
                window[s[l]] -= 1
                if window[s[l]] < hashT[s[l]]:
                    have -= 1
                l += 1

                

        return s[i:j+1] if length != float('inf') else ""
