class Solution:
    def hammingWeight(self, n: int) -> int:
        if not n:
            return 0
        count = 0
        while n > 0:
            if n % 2:
                count += 1
            n >>= 1
        return count
