class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ret = 0;
        rookpos = [-1,-1];
        for row in range(8):
            pawn = rook = 0;
            for col in range(8):
                if (board[row][col] == "p"):
                    if (rook):
                        ret += 1;
                        break;
                    else:
                        pawn = 1;
                if (board[row][col] == "R"):
                    if (pawn):
                        ret += 1;
                        pawn = 0;
                    rook = 1;
                    rookpos = [row, col];
                if (board[row][col] == "B"):
                    pawn = rook = 0;
            if (rookpos[0] >= 0):
                break;
        row,col = rookpos;
        while (row >= 0):
            if (board[row][col] == "B"):
                break;
            if (board[row][col] == "p"):
                ret += 1;
                break;
            row -= 1;
        row,col = rookpos;
        while (row < 8):
            if (board[row][col] == "B"):
                break;
            if (board[row][col] == "p"):
                ret += 1;
                break;
            row += 1;
        return ret;
            
                    
            
