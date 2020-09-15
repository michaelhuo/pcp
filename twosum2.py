from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length < 2:
            return
        left, right = 0, length - 1
        while left < right:
            value = nums[left] + nums[right]
            if value == target:
                return [left, right]
            elif value > target:
                right -= 1
            else:
                left += 1

        return


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))