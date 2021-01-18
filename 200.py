class DLinkedNode():
    def __init__(self, key = 0, value = 0, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        
class LRUCache():
    # m1 01162021
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
            return
        if self.size == self.capacity:
            self._remove_node(self.tail.prev)
            self.size -= 1
        node = DLinkedNode(key, value)
        self.cache[key] = node
        self._add_node(node)
        self.size += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
