class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        q = x
        result = 0
        while q:
            q, r = divmod(q, 10)
            result = result * 10 + r
        if result > 2 ** 31 - 1:
            result = 0
        return sign * result
