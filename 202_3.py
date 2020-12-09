class Solution:
    def isHappy(self, n: int) -> bool:
        def next(n: int) -> int:
            ans = 0
            while n > 0:
                n, digit = divmod(n, 10)
                ans += digit ** 2
            return ans
        slow = n
        fast = next(n)
        while fast != 1 and slow != fast:
            slow = next(slow)
            fast = next(next(fast))
        return fast == 1
