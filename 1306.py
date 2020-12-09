class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def visit(index: int) -> bool:
            if 0 <= index < size and index not in visited:
                value = arr[index]
                if value == 0:
                    return True
                else:
                    visited.add(index)
                    if visit(index + arr[index]):
                        return True
                    if visit(index - arr[index]):
                        return True
            return False
        size = len(arr)
        visited = set()
        return visit(start)
    
