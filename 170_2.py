class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.is_sorted = False
        
    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.array.append(number)
        self.is_sorted = False

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if len(self.array) < 2:
            return False
        if not self.is_sorted:
            self.array.sort()
            self.is_sorted = True
        size = len(self.array)
        low = 0
        high = size - 1
        while low < high:
            v = self.array[low] + self.array[high]
            if v == value:
                return True
            elif v < value:
                low += 1
            else:
                high -= 1
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
