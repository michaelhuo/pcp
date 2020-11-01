class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        hash_set = set(nums)
        hash_map = {}
        for n in nums:
            if n + 1 in hash_set:
                hash_map[n] = n + 1
        count = 1
        max_count = 1
        for n in hash_map.keys():
            count = 1
            m = n
            while hash_map[m] in hash_map:
                count += 1
                m = hash_map[m]
            max_count = max(max_count, count + 1)
        return max_count

        

