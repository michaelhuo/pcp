class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        size = len(nums)
        max_index = 0
        for index, n in enumerate(nums):
            if index <= max_index:
                max_index = max(max_index, index + n)
            else:
                return False
        return True
            
