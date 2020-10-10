class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []
        nums.sort()
        mapping = {}
        for i, n in enumerate(nums):
            if n not in mapping:
                mapping[n] = (i,i + 1)
            else:
                mapping[n] = (mapping[n][0], i + 1)
        print(nums)
        print(mapping)
        ans = []
        i = 0
        j = length - 1
        while i < j - 1:
            n = - nums[i] - nums[j]
            if n in mapping:
                s,e = mapping[n]
                k = max(i + 1, s)
                while k < min(j,e):
                    lst = [nums[i], nums[k], nums[j]]
                    if lst not in ans:
                        ans.append(lst)
                    k += 1
            if n >= 0:
                i += 1
            else:
                j -= 1

        return ans
                    
