class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.index = -1
        self.data = []
        self.size = 0
        if not v:
            return
        for lst in v:
            for i in lst:
                self.data.append(i)
        self.size = len(self.data)
        if self.size > 0:
            self.index = 0

    def next(self) -> int:
        if self.hasNext():
            ans = self.data[self.index]
            self.index += 1
            return ans
        else:
            raise(StopIteration)

    def hasNext(self) -> bool:
        if self.index != -1 and self.index < self.size:
            return True
        return False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()`
