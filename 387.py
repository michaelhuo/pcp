class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        ss = {}
        length = len(s)
        for i, c in enumerate(s):
            if c in ss:
                ss[c] = length
            else:
                ss[c] = i
        result = length
        for i in ss.values():
            if i < result:
                result = i
        if result == length:
            return -1
        else:
            return result
