class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1 and matrix[0][0] != target:
            return False
        low, high = 0, m - 1
        while low < high:
            mid = (low + high) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid
        if low > high:
            row_index = high
        elif low == high:
            if matrix[low][0] == target:
                return True
            elif matrix[low][0] > target:
                row_index = high - 1
            else:
                row_index = high
        else:
            row_index = row

        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if matrix[row_index][mid] < target:
                low = mid + 1
            else:
                high = mid
        if low > high or (low == high and matrix[row_index][low] != target):
            return False
        else:
            return True
        
        
                
