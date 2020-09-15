from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, val in enumerate(nums):
            hash_map[val] = idx
        for idx, val in enumerate(nums):
            if target - val in hash_map:
                idx2 = hash_map[target - val]
                if idx != idx2:
                    return [idx, idx2]


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))