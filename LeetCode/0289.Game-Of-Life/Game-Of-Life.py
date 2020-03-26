class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbors = 0;
                for x in range(3):
                    for y in range(3):
                        
                        if i-1+x >= 0 and i-1+x < len(board) and j-1+y >= 0 and j-1+y < len(board[0]) and board[i-1+x][j-1+y] > 0: 
                            neighbors += 1;
                        #print [i, j, x, y, i-1+x, j-1+y, neighbors]
                if board[i][j] == 1: board[i][j] = neighbors;
                else: board[i][j] = -neighbors;
        #print board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1 or board[i][j] == 2: board[i][j] = 0;
                elif board[i][j] == 3 or board[i][j] == 4: board[i][j] = 1;
                elif board[i][j] > 4: board[i][j] = 0;
                elif board[i][j] == -3: board[i][j] = 1;
                elif board[i][j] < 0: board[i][j] = 0;
                            
                
                    

