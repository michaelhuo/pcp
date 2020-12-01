class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size < 2:
            return
        low, high = 0, size - 1
        while low < high:
            if nums[low] == 0:
                low += 1
            elif nums[high] == 2:
                high -= 1
            elif nums[low] == 2:
                nums[low], nums[high] = nums[high], nums[low]
                high -= 1
            elif nums[high] == 0:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1              
            else:
                i = low
                while i <= high:
                    if nums[i] == 2:
                        nums[i], nums[high] = nums[high], nums[i]
                        high -= 1
                        good = False
                    elif nums[i] == 0:
                        nums[i], nums[low] = nums[low], nums[i]
                        low += 1
                        good = False
                    else:
                        i += 1
                break
