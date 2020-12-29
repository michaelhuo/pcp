from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size < 2:
            return nums
        if size == 2:
            if nums[0] == nums[1]:
                return [nums[0],]
            else:
                return nums
        threshold = size // 3
        count1, count2, num1, num2 = 0, 0, None, None
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                num1 = num
                count1 += 1
            elif count2 == 0:
                num2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
                
        threshold = size // 3
        answer = []
        counts = Counter(nums)
        for num, count in counts.items():
            if count > threshold:
                answer.append(num)
        return answer
    
        for num in (num1, num2):
            if nums.count(num) > threshold:
                answer.append(num)
        
        return result
