class TicTacToe(object):
    def __init__(self, n):
        self.row = [0] * n
        self.col = [0] * n
        self.diagonal = 0
        self.antidiagonal = 0
        self.n = n

    def move(self, row, col, player):
        score = 1 if player == 1 else -1
        self.row[row] += score
        self.col[col] += score
        if row == col:
            self.diagonal += score
        if row + col == self.n - 1:
            self.antidiagonal += score
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diagonal) == self.n or abs(self.antidiagonal) == self.n:
            return player
        return 0

