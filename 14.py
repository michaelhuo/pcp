from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        n = len(strs)
        if n < 1:
            return output
        l1 = strs[0]
        if len(l1) < 1:
            return output
        lengths = [len(l) for l in strs]
        min_len = min(lengths)
        idx = 0
        stop = False
        for idx in range(min_len):
            c = l1[idx]
            for l in strs[1:]:
                if l[idx] != c:
                    stop = True
                    break
            if stop:
                break
            output = output + c

        return output
