class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(len(s1) - 1, -1, -1):
            dp[i][-1] = dp[i + 1][-1] + ord(s1[i])
        for i in range(len(s2) - 1, -1, -1):
            dp[-1][i] = dp[-1][i + 1] + ord(s2[i])

        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    t1 = dp[i + 1][j] + ord(s1[i])
                    t2 = dp[i][j + 1] + ord(s2[j])
                    dp[i][j] = min(t1, t2)

        return dp[0][0]