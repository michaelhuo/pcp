class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return
        i = m - 1
        j = n - 1
        for k in range(m + n - 1, -1, -1):
            if i < 0:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            elif j < 0:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        