class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 2 and nums[0] != target:
            return -1
        size = len(nums)
        low, high = 0, size - 1
        while low < high:
            
            mid = low + (high - low) // 2
            print(low,mid,high)
            #pivot not in current range
            if nums[low] < nums[high]:
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            #pivot in current range
            else:
                #pivot in lower range
                if nums[mid] < nums[high]:
                    #target in higher range
                    if nums[mid] < target <= nums[high]:
                        low = mid + 1
                    #target in lower range with pivot
                    else:
                        high = mid
                #pivot in higher range
                else:
                    #target in lower range
                    if nums[low] <= target <= nums[mid]:
                        high = mid
                    #target in higher range with pivot
                    else:
                        low = mid + 1
        if low < size and nums[low] == target:
            return low
        else:
            return -1                                                                                                                                                                                                                                                                                                                       
            
        
