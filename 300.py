class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return size
        dp = [1] * size
        ans = 1
        for i, n in enumerate(nums):
            for j in range(i):
                if n > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])
        return ans
            
