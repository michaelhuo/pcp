class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        length = len(nums)
        nums.sort()
        hash_map = {n:i for i,n in enumerate(nums)}
        result = []
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    s = nums[i] + nums[j] + nums[k]
                    key = target - s
                    if key in hash_map:
                        l = hash_map[key]
                        if l == i or l == j or l == k:
                            continue
                        lst = sorted([nums[i], nums[j], nums[k], key])
                        if lst not in result:
                            result.append(lst)
        return result
