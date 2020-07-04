class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row0 = col0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True
                break
                
        for j in range(n):
            if matrix[0][j] == 0:
                row0 = True
                break
                
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    
        for i in range(m):
            if col0: matrix[i][0] = 0
            
        for j in range(n):
            if row0: matrix[0][j] = 0
                
