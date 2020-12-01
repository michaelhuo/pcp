class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        mark_first_col = False
        for row in range(n_rows):
            if matrix[row][0] == 0:
                mark_first_col = True
            for col in range(1, n_cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        for row in range(1, n_rows):
            for col in range(1, n_cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        if matrix[0][0] == 0:
            for col in range(1, n_cols):
                matrix[0][col] = 0
        if mark_first_col:
            for row in range(0, n_rows):
                matrix[row][0] = 0
