class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.size = n
        self.board = [[0] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = player
        diag_same1 = True
        diag_same2 = True
        n = self.size
        for i in range(n):
            if self.board[i][0] != 0:
                col_same = True
                for j in range(1, n):
                    if self.board[i][j] != self.board[i][0]:
                        col_same = False
                        break
                if col_same:
                    return self.board[i][0]
            if self.board[0][i] != 0:
                row_same = True
                for j in range(1, n):
                    if self.board[j][i] != self.board[0][i]:
                        row_same = False
                        break
                if row_same:
                    return self.board[0][i]
            if self.board[i][i] != self.board[0][0]:
                diag_same1 = False
            if self.board[i][n - i -1] != self.board[0][n - 1]:
                diag_same2 = False
        if diag_same1 and self.board[0][0] != 0:
            return self.board[0][0]
        if diag_same2 and self.board[0][n - 1] != 0:
            return self.board[0][n - 1]
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
