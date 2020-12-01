class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            k = str(sorted(s))
            if k in groups:
                groups[k].append(s)
            else:
                groups[k] = [s]
        result = []
        for k in groups.keys():
            result.append(groups[k])
        return result
