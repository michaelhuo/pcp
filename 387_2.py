import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        counter = collections.Counter(s)
        for idx,ch in enumerate(s):
            if counter[ch] == 1:
                return idx
        return -1
