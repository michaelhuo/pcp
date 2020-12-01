class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            value = numbers[low] + numbers[high]
            if value == target:
                return [low + 1, high + 1]
            elif value < target:
                low += 1
            else:
                high -= 1
        raise(ValueError)
    
