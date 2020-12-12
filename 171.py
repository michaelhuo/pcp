class Solution:
    def titleToNumber(self, s: str) -> int:
        def val(c: str) -> int:
            return ord(c) - ord('A') + 1
        answer = 0
        for c in s:
            n = val(c)
            answer = answer * 26 + n
        return answer
