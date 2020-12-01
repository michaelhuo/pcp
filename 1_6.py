class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in hash_map:
                j = hash_map[m]
                return [i, j]
            hash_map[n] = i
        return []
        

