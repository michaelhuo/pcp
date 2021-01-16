class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        print("m2 1/15/2021")
        def merge_sort(nums1: List[int], nums2: List[int]) -> List[int]:
            if not nums1:
                return nums2
            if not nums2:
                return nums1
            nums = []
            m = len(nums1)
            n = len(nums2)
            i, j = 0, 0
            while i < m and j < n:
                if nums1[i] < nums2[j]:
                    nums.append(nums1[i])
                    i += 1
                else:
                    nums.append(nums2[j])
                    j += 1
            while i < m:
                nums.append(nums1[i])
                i += 1
            while j < n:
                nums.append(nums2[j])
                j += 1
            return nums
        
        nums = merge_sort(nums1, nums2)
        m = len(nums1)
        n = len(nums2)
        size = m + n
        if size == 1:
            return float(nums[0])
        elif size % 2 == 0:
            return (nums[size // 2] + nums[size // 2 - 1]) / 2.0
        else:
            return float(nums[size // 2])

