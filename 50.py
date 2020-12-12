import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 and n < 0:
            raise ValueError()
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        ans = 1
        factor = x
        while n > 0:
            if n % 2 == 1:
                ans *= factor
            factor *= factor
            n //= 2
            
        return ans
