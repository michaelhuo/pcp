class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        bitmask = 0
        n = length - 1
        for n in nums:
            i = 1 << n
            if bitmask & i:
                return n
            else:
                bitmask = bitmask | i

