class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return None
        m = len(board)
        n = len(board[0])
        if m == n == 1:
            board[0][0] = 0
            return None
        for i in range(m):
            for j in range(n):
                c = 0
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        if 0 <= ii < m and 0 <= jj < n:
                            c += board[ii][jj] % 10
                c -= board[i][j] % 10
                board[i][j] = c * 10 + board[i][j] % 10
        for i in range(m):
            for j in range(n):
                num, state = divmod(board[i][j], 10)
                new_state = 0
                if state:
                    if num == 2 or num == 3:
                        new_state = 1
                else:
                    if num == 3:
                        new_state = 1
                board[i][j] = new_state
                        
