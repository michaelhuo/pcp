from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True
        for i in range(1, length + 1):
            idx = i - 1
            for w in wordDict:
                l = len(w)
                if dp[i - 1] and s[idx : idx + l] == w:
                    dp[i + l - 1] = True
        print(dp)
        return dp[length]

if __name__ == "__main__":
    print(Solution().wordBreak("leetcode", ["leet","code"]))