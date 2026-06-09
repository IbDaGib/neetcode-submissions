class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        countT = Counter(t)
        window = defaultdict(int)

        matches = 0
        res = [-1,-1]
        resLen = float('inf')

        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == countT[s[r]]:
                matches += 1


            while matches == len(countT):
                if r-l+1 < resLen:
                    resLen = r-l+1
                    res = [l,r]

                window[s[l]] -= 1
                if window[s[l]] + 1 == countT[s[l]]:
                    matches -= 1
                l += 1
              

            


        return s[res[0]:res[1]+1] if resLen != float('inf') else ""
