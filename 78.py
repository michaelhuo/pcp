class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(inset: List[int], nums: List[int]) -> None:
            for i, n in enumerate(nums):
                nums[0], nums[i] = nums[i], nums[0]
                if inset and n > inset[-1] or not inset:
                    answer.append(inset + [n])
                    backtracking(inset + [n], nums[1:])
                    
        answer = [[],]
        backtracking([], nums)
        return answer
        
