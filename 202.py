class Solution:
    def isHappy(self, n: int) -> bool:
        def next(n: int) -> int:
            ans = 0
            while n > 0:
                ans += (n % 10) ** 2
                n //= 10
            return ans
        if n < 1:
            return False
        nums = set()
        num = n
        while num != 1:
            if num in nums:
                return False
            nums.add(num)
            num = next(num)
        return True
