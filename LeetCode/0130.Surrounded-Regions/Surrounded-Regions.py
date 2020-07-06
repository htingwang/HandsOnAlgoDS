class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        
        m, n = len(board), len(board[0])
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == 'O': 
                    board[i][j] = 'E'
                    queue.append((i, j))
                    
        while queue:
            i, j = queue.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                    board[ni][nj] = 'E'
                    queue.append((ni, nj))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == 'E': board[i][j] = 'O'
                    
        
