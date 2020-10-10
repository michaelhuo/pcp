class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        j = 0
        result = 0
        indices = {}
        for i, c in enumerate(s):
            if c in indices and indices[c] >= j:
                index = indices[c]
                result = max(result, i - j)
                j = index + 1
            indices[c] = i
        result = max(result, len(s) - j)
        return result
