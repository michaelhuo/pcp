from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size < 2:
            return nums
        if size == 2:
            if nums[0] == nums[1]:
                return [nums[0],]
            else:
                return nums
        threshold = size // 3
        answer = []
        counts = Counter(nums)
        for num, count in counts.items():
            if count > threshold:
                answer.append(num)
        return answer

