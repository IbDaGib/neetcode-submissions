class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            s = ''.join(str(len(s)) + '#' + s)
            res += ''.join(s)

        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])     
            content = s[j + 1 : j + 1 + length]
            res.append(content)
            i = j + 1 + length   
        

        return res
