class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(nums: List[int], value: int) -> Set[Tuple[int]]:
            size = len(nums)
            i = 0
            j = size - 1
            result = set()
            while i < j:
                v = nums[i] + nums[j]
                if v > value:
                    j -= 1
                elif v < value:
                    i += 1
                else:
                    t = tuple(sorted([nums[i], nums[j]]))
                    if t not in result:
                        result.add(t)
                    i += 1
                    j -= 1
            return result
        
        if not nums:
            return []
        size = len(nums)
        if size < 3:
            return []
        nums.sort()
        triplets = set()

        for k in range(size):
            n = nums[k+1:]
            ts = two_sum(n, -nums[k])
            for n1,n2 in ts:
                triplet = tuple(sorted([n1, n2, nums[k]]))
                if triplet not in triplets:
                    triplets.add(triplet)
        return [[i,j,k] for i,j,k in triplets]
                
