class Solution:
    def isHappy(self, n: int) -> bool:
        def next(n: int) -> int:
            ans = 0
            while n > 0:
                n, digit = divmod(n, 10)
                ans += digit ** 2
            return ans
        nums = set()
        num = n
        while num != 1:
            if num in nums:
                return False
            nums.add(num)
            num = next(num)
        return num == 1
