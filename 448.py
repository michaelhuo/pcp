class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        length = len(nums)

        for j in range(length):
            n = nums[j]
            while True:
                i = n - 1
                m = nums[i]
                if m == n:
                    break
                else:
                    nums[i] = n
                    n = m
        return [i + 1 for i, n in enumerate(nums) if i != n - 1]


            
            
