class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        length = len(nums)
        answer = [0] * length
        answer[0] = 1
        for i in range(length - 1):
            answer[i + 1] = answer[i] * nums[i]
        R = 1
        for i in reversed(range(length -1)):
            R = R * nums[i + 1]
            answer[i] = answer[i] * R
        
        return answer
