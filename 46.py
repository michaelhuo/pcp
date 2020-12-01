class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(prefix: List[int], nums: List[int]) -> None:
            if not nums:
                answer.append(prefix)
            for i, n in enumerate(nums):
                backtracking(prefix + [n], nums[:i] + nums[i+1:])
        answer = []
        backtracking([], nums)
        return answer
