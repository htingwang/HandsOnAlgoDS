class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        def check_mine(i, j):
            res = 0
            for ni, nj in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    if board[ni][nj] == "M":
                        res += 1
            return res
        
        queue = collections.deque([click])
        seen = set([tuple(click)])
        while queue:
            i, j = queue.popleft()
            if board[i][j] == "M":
                board[i][j] = "X"
                return board
            num = check_mine(i, j)
            if num > 0:
                board[i][j] = str(num)
                continue
            board[i][j] = "B"
            for ni, nj in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and (ni, nj) not in seen:
                    if board[ni][nj] == "M":
                        num += 1
                    elif board[ni][nj] == "E":
                        queue.append((ni, nj))
                        seen.add((ni, nj))
        return board
                
                                                                                                                        
