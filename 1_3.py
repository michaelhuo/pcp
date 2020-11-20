class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            indices[target - n] = i
        for i, n in enumerate(nums):
            if n in indices:
                if indices[n] != i:
                    return [i, indices[n]]
        return []
