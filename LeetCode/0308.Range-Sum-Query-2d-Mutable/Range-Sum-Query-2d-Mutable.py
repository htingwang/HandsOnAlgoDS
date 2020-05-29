class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]: return
        m, n = len(matrix), len(matrix[0])
        self.mat = [[matrix[i][j] for j in range(n)] for i in range(m)]
        self.seg = collections.defaultdict(int)
        self.build(0, 0, m - 1, n - 1, 0)
        
    def build(self, r1, c1, r2, c2, idx):
        if (r2 < r1 or c2 < c1): return 0
        if (r1 == r2 and c1 == c2): self.seg[idx] = self.mat[r1][c1]
        else:
            rmid, cmid = (r1 + r2) // 2, (c1 + c2) // 2
            val = 0
            val += self.build(r1, c1, rmid, cmid, 4 * idx + 1)
            val += self.build(r1, cmid + 1, rmid, c2, 4 * idx + 2)
            val += self.build(rmid + 1, c1, r2, cmid, 4 * idx + 3)
            val += self.build(rmid + 1, cmid + 1, r2, c2 , 4 * idx + 4)
            self.seg[idx] = val
        return self.seg[idx]
    
    def _update(self, r1, c1, r2, c2, row, col, idx, val):
        if (r2 < r1 or c2 < c1 or row < r1 or row > r2 or col < c1 or col > c2): return
        self.seg[idx] += val
        if r1 ==r2 and c1 == c2: return
        else:
            rmid, cmid = (r1 + r2) // 2, (c1 + c2) // 2
            self._update(r1, c1, rmid, cmid, row, col, 4 * idx + 1, val)
            self._update(r1, cmid + 1, rmid, c2, row, col, 4 * idx + 2, val)
            self._update(rmid + 1, c1, r2, cmid, row, col, 4 * idx + 3, val)
            self._update(rmid + 1, cmid + 1, r2, c2, row, col, 4 * idx + 4, val)
            
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        self._update(0, 0, len(self.mat) - 1, len(self.mat[0]) - 1, row, col, 0, val - self.mat[row][col])
        self.mat[row][col] = val
    
    def query(self, r1, c1, r2, c2, row1, col1, row2, col2, idx):
        if (r2 < r1 or c2 < c1 or row2 < r1 or row1 > r2 or col2 < c1 or col1 > c2): return 0
        if (row2 >= r2 and row1 <= r1 and col2 >= c2 and col1 <= c1): return self.seg[idx]
        res = 0
        rmid, cmid = (r1 + r2) // 2, (c1 + c2) // 2
        res += self.query(r1, c1, rmid, cmid, row1, col1, row2, col2, 4 * idx + 1)
        res += self.query(r1, cmid + 1, rmid, c2, row1, col1, row2, col2, 4 * idx + 2)
        res += self.query(rmid + 1, c1, r2, cmid, row1, col1, row2, col2, 4 * idx + 3)
        res += self.query(rmid + 1, cmid + 1, r2, c2, row1, col1, row2, col2, 4 * idx + 4)
        return res

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.query(0, 0, len(self.mat) - 1, len(self.mat[0]) - 1, row1, col1, row2, col2, 0)
        

class NumMatrix2(object):

    def __init__(self, matrix):
        if not matrix or not matrix[0]: return
        m, n = len(matrix), len(matrix[0])
        self.mat = [[0] * n for _ in range(m)]
        self.bit = [[0] * (n + 1) for _ in range(m + 1)]    
        for i in range(m):
            for j in range(n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        diff = val - self.mat[row][col]
        i = row + 1
        while i < len(self.bit):
            j = col  + 1
            while  j < len(self.bit[0]):
                self.bit[i][j] += diff
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
        return self.query(row2 + 1, col2 + 1) - self.query(row1, col2 + 1) - self.query(row2 + 1, col1) + self.query(row1, col1)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
