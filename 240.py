class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1 and matrix[0][0] != target:
            return False
        if matrix[0][0] > target:
            return False
        low, high = 0, n - 1
        row_index, col_index = 0, 0
        row_high, col_high = 0, 0
        while low < high:
            mid = (low + high) // 2
            if matrix[row_index][mid] < target:
                low = mid + 1
            else:
                high = mid
        if low == n:
            col_high = n
        else:
            if matrix[row_index][low] == target:
                return True
            elif matrix[row_index][low] < target:
                col_high = low + 1
            else:
                col_high = low

        low, high = 0, m - 1
        while low < high:
            mid = (low + high) // 2
            if matrix[mid][col_index] < target:
                low = mid + 1
            else:
                high = mid
        if low == m:
            row_high = m
        else:
            if matrix[low][col_index] == target:
                return True
            elif matrix[low][col_index] < target:
                row_high = low + 1
            else:
                row_high = low
        for i in range(row_high):
            for j in range(col_high):
                if matrix[i][j] == target:
                    return True
        return False
