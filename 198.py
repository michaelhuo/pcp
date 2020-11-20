class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]
        elif size == 2:
            return max(nums[0], nums[1])
        else:
            dp0 = nums[0]
            dp1 = max(nums[1], nums[0])
            dp = max(dp0 + nums[2], dp1)
            for n in range(2,size):
                dp = max(dp0 + nums[n], dp1)
                dp0 = dp1
                dp1 = dp
            return dp
            
