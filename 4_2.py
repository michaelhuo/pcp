class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        print("m3 1/15/2021")
        nums = []
        if not nums1:
            nums = nums2
        if not nums2:
            nums = nums1
        if nums:
            size = len(nums)
            size2 = size // 2
            if size == 1:
                return nums[0]
            elif size % 2 == 0:
                return float(nums[size2] + nums[size2 - 1]) / 2
            else:
                return float(nums[size2])
    
        m = len(nums1)
        n = len(nums2)
        size = m + n
        low1, high1 = 0, m - 1
        low2, high2 = 0, n - 1
        count_left, count_right = 0, 0
        mid1, mid2 = 0, 0
        while low1 < high1 and low2 < high2:
            mid1 = (low1 + high1) // 2
            mid2 = (low2 + high2) // 2
            count_left = mid1 + mid2
            count_right = size - 2 - mid1 - mid2
            if count_left > 0 and count_right > 0 and count_left == count_right:
                return float((nums1[mid1] + nums2[mid2])) / 2
            elif count_left < count_right:
                if nums1[mid1] < nums2[mid2]:
                    low1 = mid1 + 1
                else:
                    low2 = mid2 + 1
            else:
                if nums1[mid1] < nums2[mid2]:
                    high2 = mid2
                else:
                    high1 = mid1
        low, high, mid = 0, 0, 0
        count_left_one, count_right_one = 0, 0
        size_one = 0
        if low1 >= high1:
            low, high = low2, high2
            size_one = n
            nums = nums2
            if nums1[mid1] > nums2[mid2]:
                count_left_one = mid1
                count_right_one = m - mid1
            else:
                count_left_one = mid1 + 1
                count_right_one = m - mid1 - 1
        elif low2 >= high2:
            low, high = low1, high1    
            nums = nums1
            size_one = m
            if nums1[mid1] > nums2[mid2]:
                count_left_one = mid2
                count_right_one = n - mid1
            else:
                count_left_one = mid2 + 1
                count_right_one = n - mid2 - 1
        while low < high:
            mid = (low + high) // 2
            count_left = count_left_one + mid
            count_right = count_right_one + size_one - mid - 1
            if count_left == count_right:
                return float(nums[mid])
            elif count_left < count_right:
                low = mid + 1
            else:
                high = mid
        if low == mid + 1:
            return float(nums[mid] + nums[mid - 1]) / 2
        elif low == mid:
            return float(nums[mid] + nums[mid -1]) / 2
            
        return None
