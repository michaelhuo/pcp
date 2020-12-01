class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False
        minimal = pivot = previous = float('inf')
        for n in nums:
            if n < minimal:
                minimal = n
            elif n > pivot:
                return True
            elif n > minimal:
                pivot = n
            previous = n
        return False
