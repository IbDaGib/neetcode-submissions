class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s in hash:
                hash[sort_s].append(s)
            else:
                hash[sort_s] = [s]
            

        return list(hash.values())