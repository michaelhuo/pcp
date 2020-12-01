class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_counts = {}
        
    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.num_counts:
            self.num_counts[number] += 1
        else:
            self.num_counts[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for n, c in self.num_counts.items():
            m = value - n
            if m == n:
                if c > 1:
                    return True
            elif m in self.num_counts:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
