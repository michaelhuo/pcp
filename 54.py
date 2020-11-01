class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        L = T = 0
        R = n - 1
        B = m - 1
        i, j = 0, 0
        dirs =[(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0
        d = 0
        output = []
        while count < m * n:
            output.append(matrix[i][j])
            di, dj = dirs[d]
            ip, jp = i + di, j + dj
            turn = False
            if jp > R:
                T += 1
                turn = True
            elif jp < L:
                B -= 1
                turn = True
            elif ip > B:
                R -= 1
                turn = True
            elif ip < T:
                L += 1
                turn = True
            if turn:
                d = (d + 1) % 4
                di, dj = dirs[d]
                i, j = i + di, j + dj
            else:
                i, j = ip, jp
            count += 1
        return output
                
        
