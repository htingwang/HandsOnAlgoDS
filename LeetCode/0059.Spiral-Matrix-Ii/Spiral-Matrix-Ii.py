class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n: return []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        di = 0
        row_min = col_min = 0
        row_max = col_max = n - 1
        row = col = 0
        
        res = [[0] * n for _ in range(n)]
        for i in range(n ** 2):
            #print(row, col, i + 1)
            res[row][col] = i + 1
            n_row = row + directions[di][0]
            n_col = col + directions[di][1]
            #print(n_row, n_col,  not row_min <= n_row <= row_max, not col_min <= n_col <= col_max, di)
            if not row_min <= n_row <= row_max or not col_min <= n_col <= col_max:
                #print(di)
                if n_col > col_max:
                    row_min += 1
                elif n_row > row_max:
                    col_max -= 1
                elif n_col < col_min:
                    row_max -= 1
                elif n_row < row_min:
                    col_min += 1
                di = (di + 1) % 4
            #print(di, row_min, row_max, col_min, col_max)
            row += directions[di][0]
            col += directions[di][1]
        return res
            
        
