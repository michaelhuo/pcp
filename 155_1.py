class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            self.min_stack.append((x, 1))
            return
        minimum, count = self.min_stack[-1]
        if x < minimum:
            self.min_stack.append((x, 1))
        elif x == minimum:
            self.min_stack[-1] = (x, count + 1)
        
        self.stack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        minimum, count = self.min_stack[-1]
        if x == minimum:
            if count > 1:
                self.min_stack[-1] = (x, count - 1)
            else:
                self.min_stack.pop()
                

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
