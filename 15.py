from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 1:
            return []
        nums.sort()
        result = []
        i = 0
        while i < n - 2:
            j = i + 1
            k = n - 1
            while j < k:
                l = nums[i] + nums[j] + nums[k]
                if l == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                elif l > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
            while i < n - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

if __name__ == "__main__":
    assert(Solution().threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]])
