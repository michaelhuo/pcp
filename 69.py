class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        low, high = 0, x // 2
        while low < high:
            mid = (low + high) // 2
            num = mid * mid
            if num < x:
                low = mid + 1
            else:
                high = mid
        if low * low <= x:
            return low
        return low - 1
