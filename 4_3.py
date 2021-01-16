import heapq
class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}
        self.heap = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            heap = []
            heapq.heappush(heap, (timestamp, value))
            self.heap[key] = heap
            hash_map = {}
            hash_map[timestamp] = value
            self.hash[key] = hash_map
        else:
            hash_map = self.hash[key]
            heap = self.heap[key]
            if timestamp in hash_map:
                hash_map[timestamp] = value
                low, high = 0, len(heap) - 1
                while low < high:
                    mid = (low + high) // 2
                    ts, value = heap[mid]
                    if ts < timestamp:
                        low = mid + 1
                    else:
                        high = mid
                ts, value = heap[low]
                if low < len(heap):
                    ts, value = heap[low]
                    if ts == timestamp:
                        heap[low] = (timestamp, value)
            else:
                self.hash[key][timestamp] = value
                heapq.heappush(self.heap[key], (timestamp, value))
        # print(self.heap)
        # print(self.hash)
  
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash:
            return ""
        if timestamp in self.hash[key]:
            #print("found in hash key = {} ts = {}".format(key, timestamp))
            return self.hash[key][timestamp]
        else:
            size = len(self.heap[key])
            low, high = 0, size - 1
            while low < high:
                mid = (low + high) // 2
                ts, value = self.heap[key][mid]
                if ts < timestamp:
                    low = mid + 1
                else:
                    high = mid
            ts, value = self.heap[key][low]
            if ts <= timestamp:
                return value
        print(self.hash)
        print(self.heap)
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
