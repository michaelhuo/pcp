class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or k < 1:
            return False
        visited = {} 
        for i, n in enumerate(nums):
            if n in visited and visited[n] >= i - k:
                return True
            visited[n] = i
        return False
