class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or k < 1:
            return False
        visited = set()
        length = len(nums)
        for i in range(min(length, k + 1)):
            n = nums[i]
            if n in visited:
                return True
            visited.add(n)
        for i in range(min(length, k + 1), length):
            j = i - k - 1
            visited.discard(nums[j])
            n = nums[i]
            if n in visited:
                return True
            visited.add(n)
            
        return False
            
