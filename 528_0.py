import random
class Solution:

    def __init__(self, w: List[int]):
        if not w:
            return
        self.w = w
        self.weight = {}
        self.size = len(w)
        self.sum = sum(self.w)
        start, end = 0, -1
        for index, weight in enumerate(w):
            end = start + weight - 1
            item = [end, weight]
            self.weight[start] = item
            start = end + 1
        
    def pickIndex(self) -> int:
        time = random.randrange(self.size)
        if time in self.weight:
            return self.weight[time][1]
        keys = sorted(self.weight.keys())
        low, high = 0, size - 1
        while low < high:
            mid = low + (high - low) // 2
            if time < keys[mid]:
                low = mid + 1
            else:
                high = mid
        if low < size and keys[low] <= time:
            key = keys[low]
            return self.weight[key][1]
        
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
