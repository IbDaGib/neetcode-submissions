class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        window = defaultdict(int)
        have = 0
        need = len(countT)
        coord = [-1,-1]
        resLen = float('inf')
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if resLen > r-l+1:
                    resLen = r-l+1
                    coord = [l,r]
                    
                window[s[l]] -= 1
                if window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        return s[coord[0]: coord[1]+1] if coord != [-1,-1] else ''

