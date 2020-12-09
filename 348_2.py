class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.size = n
        self.rows = [[0,0] for _ in range(n)]
        self.cols = [[0,0] for _ in range(n)]
        self.diags = [0] * n
        self.anti_diags = [0] * n

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
        self.rows[row][player - 1] += 1
        if self.rows[row][player -1] == self.size:
            return playera
        self.cols[col][player - 1] += 1
        if self.cols[col][player - 1] == self.size:
            return player
        if row == col:
            self.diags[row] = player
            if self.diags.count(player) == self.size:
                return player
        if row == self.size - col - 1:
            self.anti_diags[row] = player
            if self.anti_diags.count(player) == self.size:
                return player
        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
