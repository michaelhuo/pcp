class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        # if length == 1:
        #     return 1
        max_index = 0
        max_count = 0
        
        last_index = 0
        last_pre_count = 0
        last_count = 0
        pre_zero = 0

        count = 0        
        for i in range(length):
            if nums[i] == 1:
                count += 1
            else:
                last_count = last_pre_count + count + pre_zero
                if last_count > max_count:
                    max_count = last_count
                    max_index = last_index
                last_pre_count = count
                last_index = i
                count = 0
                pre_zero = 1
                
            
                
        if count > 0 or pre_zero == 1:
            last_count = last_pre_count + count + pre_zero
            if last_count > max_count:
                max_count = last_count
                max_index = last_index

        return max_count