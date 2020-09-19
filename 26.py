class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        i = 0
        for j in range(1, length):
            if nums[j - 1] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
            