class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not len(matrix[0]) : return
        print("hihihi")
        print(matrix, len(matrix[0]))
        m, n = len(matrix), len(matrix[0])
        self.s = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.s[i][j] = self.s[i - 1][j] + self.s[i][j - 1] - self.s[i - 1][j - 1] + matrix[i - 1][j - 1] 
        print(self.s)       
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.s[row2 + 1][col2 + 1] -self.s[row1][col2 + 1] - self.s[row2 + 1][col1] + self.s[row1][col1]
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
