import heapq
from collections import Counter
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            minimum = float('inf')
            for n in nums:
                if n < minimum:
                    minimum = n
            return minimum
        counts = Counter(nums)
        count = 1
        for n in sorted(counts.keys(), reverse = True):
            c = counts[n]
            if count <= k < count + c:
                return n
            count += c
        raise(ValueError)
