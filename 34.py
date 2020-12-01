class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        size = len(nums)
        low, high = 0, size - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                i = j = mid
                while i > 0 and nums[i - 1] == target:
                    i -= 1
                while j < size - 1 and nums[j + 1] == target:
                    j += 1
                return [i, j]
        return [-1, -1]
