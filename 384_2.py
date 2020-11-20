import random
class Solution:

    def __init__(self, nums: List[int]):
        self.output = nums
        self.nums = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.output = self.nums
        self.nums = self.output[:]
        return self.output

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.nums)):
            swap_index = random.randrange(i, len(self.nums))
            self.output[i], self.output[swap_index] = self.output[swap_index], self.output[i]
        #random.shuffle(output)
        return self.output
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
