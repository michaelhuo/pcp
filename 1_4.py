class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            if n in indices:
                if indices[n] != i:
                    return [indices[n], i]
            indices[target - n] = i
        return []

