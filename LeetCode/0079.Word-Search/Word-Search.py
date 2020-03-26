class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ans = False;
        path = [];
        def findword(board, word, start):   
            if len(word) == 0: return True;
            i, j = start[0], start[1];
            if i < 0 or i >= len(board) or j<0 or j >= len(board[0]): return False;
            #print [start, word, board]
            if board[i][j] == word[0]: 
                #print [i,j]
                board[i][j] = "";
                if (findword(board, word[1:], [i-1, j]) or findword(board, word[1:], [i, j-1]) or findword(board, word[1:], [i, j+1]) or findword(board, word[1:], [i+1, j])):
                    return True;
                board[i][j] = word[0];
            return False;
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (findword(board, word, [i, j])):
                    return True;
        return False;
        
