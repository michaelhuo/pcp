class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        length = len(nums)
        i = j = 0
        for j in range(length):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for j in range(i, length):
            nums[j] = 0