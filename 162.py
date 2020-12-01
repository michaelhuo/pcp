class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return 0
        i, j = 0, size - 1
        while i <= j:
            k = (i + j) // 2
            key = nums[k]
            prev = nums[k - 1] if k > 0 else float('-inf')
            succ = nums[k + 1] if k < size - 1 else float('-inf')
            if prev < key > succ:
                return k
            elif key < succ:
                i = k + 1
            else:
                j = k - 1
            
        
        
