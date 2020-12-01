class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        total = 0
        mask = 1
        for _ in range(32):
            if (x & mask) ^ (y & mask):
                total += 1
            mask <<= 1
        return total
