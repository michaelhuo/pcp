class Solution:
    def climbStairs(self, n: int) -> int:
        dp = 0
        if n == 1:
            dp = 1
        elif n == 2:
            dp = 2
        else:
            dp0 = 1 
            dp1 = 2
            for _ in range(2, n):
                dp = dp1 + dp0
                dp0 = dp1
                dp1 = dp
                
        return dp
    
