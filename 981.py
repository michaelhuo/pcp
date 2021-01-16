import heapq
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            item = {timestamp:value}
            self.data[key] = item
        else:
            item = self.data[key]
            item[timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        item = self.data[key]
        if timestamp in item:
            return item[timestamp]
        else:
            max_k = 0
            max_v = ""
            for k, v in item.items():
                if max_k < k < timestamp:
                    max_k = k
                    max_v = v
            return max_v
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
