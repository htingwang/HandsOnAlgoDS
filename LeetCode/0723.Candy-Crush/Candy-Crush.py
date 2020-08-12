class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(board), len(board[0])
        while True:
            remove = []
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 0: continue
                    x0 = x1 = i
                    y0 = y1 = j
                    while x0 >= 0 and x0 > i - 3 and board[x0][j] == board[i][j]: x0 -= 1
                    while x1 < m and x1 < i + 3 and board[x1][j] == board[i][j]: x1 += 1
                    while y0 >= 0 and y0 > j - 3 and board[i][y0] == board[i][j]: y0 -= 1
                    while y1 < n and y1 < j + 3 and board[i][y1] == board[i][j]: y1 += 1
                    if (x1 - x0 > 3 or y1 - y0 > 3): remove.append((i, j))
            if not remove: break
            for i, j in remove: board[i][j] = 0
            for j in range(n):
                t = m - 1
                for i in range(m - 1, -1, -1):
                    if board[i][j]: 
                        board[t][j], board[i][j] = board[i][j], board[t][j]
                        t -= 1
        return board
        
