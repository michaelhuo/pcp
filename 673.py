class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 1:
            return 0
        dp = [[0] * length for _ in range(length)]
        max_num = 1
        for i in range(length):
            dp[i][i] = 1
        for i in range(length - 1):
            for j in range(i + 1, length):
                for k in range(j - 1, i - 1, -1):
                    if nums[j] > nums[k]:
                        dp[i][j] = max(dp[i][j], dp[i][k] + 1)
                        max_num = max(max_num, dp[i][j])
        count = 0
        for i in range(length):
            for j in range(length):
                if dp[i][j] == max_num:
                    count += 1
        print(max_num, count)
        print(dp)
        return count

