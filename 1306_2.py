from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        size = len(arr)
        visited = set()
        queue = deque()
        queue.append(start)
        while queue:
            index = queue.popleft()
            if index not in visited:
                visited.add(index)
                value = arr[index]
                if value == 0:
                    return True
                if index + value < size:
                    queue.append(index + value)
                if index - value >= 0:
                    queue.append(index - value)
        return False
