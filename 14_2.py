class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        count = len(strs)
        length = float('inf')
        index = -1
        for i,s in enumerate(strs):
            l = len(s)
            if l < length:
                index = i
                length = l
        offset = -1
        for i, c in enumerate(strs[index]):
            stop = False
            for j in range(count):
                if strs[j][i] != c:
                    stop = True
                    break
            if stop:
                break
            offset = i
        return strs[index][:offset + 1]
