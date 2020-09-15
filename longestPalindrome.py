class Solution:
    # def __init__(self) -> None:
    #     self.max_len = 0
    #     self.max_str = ""

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""
        self.max_len = 1
        self.max_str = s[0]
        longest(s)
        return max_str

    def _longestPalindrome(self, s: str) -> None:
        if len(s) <= max_len:
            return
        if isPalindromic(s):
            if len(s) > max_Len:
                self.max_str = s
                self.max_len = len(s)
            return
        longest(s[1:])
        longest(s[:-1])

    def isPalindromic(self, s: str) -> bool:
        if not s:
            return False
        if len(s) == 1:
            return True
        if s == s[::-1]:
            return True
        return False


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s
        p = [[False] * length for _ in range(length)]
        max_value = 1
        left, right = 0, 0

        for i in range(length):
            p[i][i] = True

        print(p)

        for j in range(1, length):
            i = j - 1

            while (s[i] == s[j] and p[i + 1][j - 1] and i > 0):
                p[i][j] = True
                i -= 1
            if (j - i + 1 > max_value):
                max_value = j - i + 1
                left = i
                right = j

            print(max_value, left, right)
            print(p)
        return s[left: right + 1]


if __name__ == "__main__":
    print(Solution().longestPalindrome("ababa"))


if __name__ == "__main__":
    s = "abcbb"
    t = Solution().longstPalindrome(s)
    print(s, t)