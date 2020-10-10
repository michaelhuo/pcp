class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue =[]
        self.size = size

    def next(self, val: int) -> float:
        self.queue.append(val)
        return sum(self.queue[-self.size:]) / min(len(self.queue), self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
