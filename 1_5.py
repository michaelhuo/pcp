class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {target - n:i for i,n in enumerate(nums)}
        for i, n in enumerate(nums):
            if n in hash_map:
                j = hash_map[n]
                if j != i:
                    return [i, j]
        return []
        

