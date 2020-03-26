class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        todo = 0
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        region = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    todo += 1
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    region[(i // 3) * 3 + j // 3].add(board[i][j])

        self.dfs(board, 0, 0, todo, row, col, region)
        
    def dfs(self, board, i, j, todo, row, col, region):
        if todo == 0: 
            return 1
        while board[i][j] != ".":
            pos = i * 9 + j + 1
            i = pos / 9
            j = pos % 9
        for val in "123456789":            
            if val not in (row[i] | col[j] | region[(i // 3) * 3 + j // 3]):    
                board[i][j] = val
                row[i].add(val)
                col[j].add(val)
                region[(i // 3) * 3 + j // 3].add(val)
                if self.dfs(board, i, j, todo - 1, row, col, region):
                    return 1
                board[i][j] = "."
                row[i].remove(val)
                col[j].remove(val)
                region[(i // 3) * 3 + j // 3].remove(val)
        return 0
        
