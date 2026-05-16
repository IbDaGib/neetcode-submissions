class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list[str])

        for s in strs:
            sort_s = "".join(sorted(s))
            count[sort_s].append(s)

        return list(count.values())

        