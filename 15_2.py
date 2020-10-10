class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []
        ans = []
        for i,n in enumerate(nums):
            indices = {}
            target = -n
            for j in range(i + 1, length):
                if nums[j] in indices:
                    if nums[j] * 2 == target:
                        lst = [nums[i], nums[j], nums[indices[nums[j]]]]
                        lst.sort()
                        if lst not in ans:
                            ans.append(lst)
                else:
                    indices[nums[j]] = j
            for j in range(i + 1, length):
                if target - nums[j] in indices and indices[target - nums[j]] != j:
                    lst = [nums[i], nums[j], nums[indices[target - nums[j]]]]
                    lst.sort()
                    if lst not in ans:
                        ans.append(lst)
        return ans
                    
