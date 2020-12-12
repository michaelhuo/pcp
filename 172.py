class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        num = 5
        while num <= n:
            ans += n // num
            num *= 5
        return ans
