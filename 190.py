class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        mask = 1 << 31
        mask2 = 1
        for _ in range(32):
            if mask & n:
                output |= mask2
            mask >>= 1
            mask2 <<= 1
        return output
        
