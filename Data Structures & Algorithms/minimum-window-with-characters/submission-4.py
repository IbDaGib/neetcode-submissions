class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "": return ""
        if t == s: return t

        countT = Counter(t)
        window = defaultdict(int)

        matches = 0

        res = [-1,-1]
        resLen = float('inf')

        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                matches += 1
                
            while matches == len(countT):
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    matches -= 1
                l += 1
            
        l,r = res
                

        return s[l:r+1] if resLen != float('inf') else ""

            
            
