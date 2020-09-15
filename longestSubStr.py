class Solution:
    def lengthOfLongestSubstring0(self, s: str) -> int:
        if not s:
            return 0
        max_len = 1
        str_len = len(s)
        sub_str = {}
        for i in range(str_len):
            cur_len = 1
            sub_str = {s[i]}
            j = i + 1
            while j < str_len:
                c = s[j]
                j += 1
                if c not in sub_str:
                    sub_str.add(c)
                    cur_len += 1
                    if cur_len > max_len:
                        max_len = cur_len
                else:
                    break
        return max_len

    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            if not s:
                return 0
            if len(s) < 2:
                return len(s)

            l = [-1 for _ in range(256)]

            max_len = 0
            index = -1
            for i, c in enumerate(s):
                prev_loc = l[ord(c)]
                l[ord(c)] = i
                if prev_loc > index:
                    index = prev_loc
                max_len = max(max_len, i - index)

            return max_len