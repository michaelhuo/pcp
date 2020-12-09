import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = {}
        self.queue = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hash_map:
            return False
        self.queue.append(val)
        self.hash_map[val] = len(self.queue) - 1

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hash_map:
            return False
        index = self.hash_map[val]
        key = self.queue[-1]
        self.queue[index] = key
        self.hash_map[key] = index
        self.queue.pop()
        del self.hash_map[val]
        return True
    
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = random.randrange(len(self.queue))
        return self.queue[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
