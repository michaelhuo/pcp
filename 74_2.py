class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def index(i: int) -> int:
            return matrix[i // n][i % n]
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        size = m * n
        if m == 1 and n == 1 and matrix[0][0] != target:
            return False
        low, high = 0, size - 1
        while low < high:
            mid = (low + high) // 2
            if index(mid) < target:
                low = mid + 1
            else:
                high = mid
        if low < size and index(low) == target:
            return True
        else:
            return False

