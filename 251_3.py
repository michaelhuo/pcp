class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.outer = 0
        self.inner = 0
        self.vector = v
            
    def _next(self):
        while self.outer < len(self.vector) and not self.vector[self.outer]:
            self.outer += 1
            self.inner = 0
            
    def next(self) -> int:
        self._next()
        ans = self.vector[self.outer][self.inner]
        self.inner += 1
        if self.inner == len(self.vector[self.outer]):
            self.outer += 1
            self.inner = 0
        return ans

    def hasNext(self) -> bool:
        self._next()
        return self.outer < len(self.vector)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
