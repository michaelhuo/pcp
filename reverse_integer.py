from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        value = abs(x)
        is_minus = True if x != value else False
        result = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        while value > 0:
            result = result * 10 + value % 10
            value //= 10

        if is_minus:
            result = - result

        if result > INT_MAX or result < INT_MIN:
            result = 0

        return result


if __name__ == "__main__":
    assert (Solution().reverse(123) == 321)
    assert (Solution().reverse(-123) == -321)
    assert (Solution().reverse(120) == 21)

