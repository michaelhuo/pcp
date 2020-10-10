class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        min_index = 0
        larger_index = -1
        for i in range(1, len(nums)):
            if nums[i] <= nums[min_index]:
                min_index = i
            else:
                if larger_index != -1 and nums[i] > nums[larger_index]:
                    return True
                else:
                    larger_index = i
        return False
