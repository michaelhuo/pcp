class Solution:
    def convertToTitle(self, n: int) -> str:
        def val(n: int) -> str:
            return chr(ord('A') + n)
        num = n
        ans = []
        while num > 0:
            num, digit = divmod(num - 1, 26)
            ans.append(val(digit))
        ans.reverse()
        return "".join(ans)
