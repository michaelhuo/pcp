import heapq
from collections import Counter
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return heapq.nlargest(k, nums)[-1]
        def partition(left: int, right: int) -> int:
            if left == right:
                return left
            index = right
            i1 = random.randint(left, right)
            i2 = random.randint(left, right)
            i3 = random.randint(left, right)
            #print(i1, i2, i3)
            if nums[i1] < nums[i2]:
                if nums[i2] < nums[i3]:
                    index = i2
                elif nums[i1] < nums[i3]:
                    index = i1
                else:
                    index = i3
            else:
                if nums[i2] > nums[i3]:
                    index = i2
                elif nums[i1] < nums[i3]:
                    index = i1
                else:
                    index = i2
                    
            pivot = nums[index]
            nums[index], nums[right] = nums[right], nums[index]
            index = left
            i = index
            while i < right:
                if nums[i] < pivot:
                    if index < i:
                        nums[i], nums[index] = nums[index], nums[i]
                    index += 1
                i += 1
            if index < right:
                nums[index], nums[right] = nums[right], nums[index]
            return index

        def quick_select(left: int, right: int, k: int) -> int:
            pivot_index = partition(left, right)

            if pivot_index == k - 1:
                return nums[pivot_index]
            elif pivot_index > k - 1:
                return quick_select(left, pivot_index, k)
            else:
                return quick_select(pivot_index + 1, right, k)
        
        size = len(nums)
        return quick_select(0, size - 1, size - k + 1)
