class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board or not board[0]: return 0
        res = 0
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if (board[i][j] == "." or (i > 0 and board[i - 1][j] == 'X') or (j > 0 and board[i][j - 1] == "X")): continue
                res += 1
        return res

        
