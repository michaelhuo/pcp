class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.x = 0
        self.y = 0
        self.data = v
        while self.x < len(self.data) and not self.data[self.x]:
            self.x += 1
        

    def next(self) -> int:
        ans = self.data[self.x][self.y]
        self.y += 1
        if self.y == len(self.data[self.x]):
            self.x += 1
            self.y = 0
        while self.x < len(self.data) and not self.data[self.x]:
            self.x += 1
            self.y = 0
        return ans

    def hasNext(self) -> bool:
        if self.x < len(self.data):
            return True
        else:
            return False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
