class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [[1] * n for __ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row][col - 1] + dp[row - 1][col]
        return dp[m - 1][n - 1]
