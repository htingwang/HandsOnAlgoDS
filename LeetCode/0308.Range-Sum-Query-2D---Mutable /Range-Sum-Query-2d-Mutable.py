class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]: return
        
        m, n = len(matrix), len(matrix[0])
        self.m, self.n = m, n
        self.mat = [[0] * (n) for _ in range(m)]
        self.bit = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.update(i, j, matrix[i][j])
        

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        delta = val - self.mat[row][col]
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] += delta
                j += (j & -j)
            i += (i & -i)
        self.mat[row][col] = val
            
    def query(self, row, col):
        res = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                res += self.bit[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return res
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        #print(row1, col1, row2, col2)
        return self.query(row2 + 1, col2 + 1) - self.query(row1, col2 + 1) - self.query(row2 + 1, col1) + self.query(row1, col1)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
