class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        print("m0 1/16/2021")
        size = len(nums)
        if size == 1:
            return nums[0]
        n = size - 1
        visited = set()
        for i, n in enumerate(nums):
            if n in visited:
                return n
            visited.add(n)
