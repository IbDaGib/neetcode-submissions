class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]

        hash = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in hash:
                hash[sortedWord] = [word]
            else:
                hash[sortedWord].append(word)
        res = []
        for value in hash.values():
            res.append(value)
        return res
        