class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += "".join(str(len(s)) + '#' + s)

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # number
            i = j + 1
            j = i + length
            res.append(s[i:j]) # string
            i = j # moves i to start of next string

        return res