class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        length = len(nums)
        i = 0
        n = nums[0]
        for i, n in enumerate(nums):
            if n == i + 1 or n < 1 or n > length:
                continue
            j = n - 1
            m = nums[j]
            nums[j] = n
            while m != n and 0 < m <= length:
                j = m - 1
                n = m
                m = nums[j]
                nums[j] = n
                
        for i, n in enumerate(nums, 1):
            if i != n:
                return i
        return length + 1
            
            
