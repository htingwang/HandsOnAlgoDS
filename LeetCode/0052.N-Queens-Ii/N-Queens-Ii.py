class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        cols = [0] * n
        dia1 = [0] * (2 * n + 1)
        dia2 = [0] * (2 * n + 1)
        self.res = 0
        
        def check(row, col):
            return not (cols[col] + dia1[row + col] + dia2[row - col])
        
        def update(row, col, seen):
            cols[col] = seen
            dia1[row + col] = seen
            dia2[row - col] = seen
       
        
        def backtrack(row):
            if row == n:
                self.res += 1
                return
            
            for col in range(n):
                if check(row, col):
                    update(row, col, 1)
                    backtrack(row + 1)
                    update(row, col, 0)
        backtrack(0)   
        return self.res
