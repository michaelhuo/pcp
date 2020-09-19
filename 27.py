class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        length = len(nums)
        j = length - 1
        i = 0
        while i <= j:
            if nums[i] == val:
                while j > i and nums[j] == val:
                    j -= 1
                if j <= i:
                    j = i - 1
                    break
                nums[i] = nums[j]
                j -= 1
            i += 1
        return j + 1