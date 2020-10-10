class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        hash_map = {}
        for s in strs:
            key = str(sorted(s))
            if key not in hash_map:
                hash_map[key] = [s]
            else:
                hash_map[key].append(s)
        output = [l for l in hash_map.values()]
        return output
