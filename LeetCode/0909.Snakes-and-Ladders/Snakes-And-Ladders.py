from collections import deque
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        if not board or not board[0]: return 0
        res = 0
        m, n = len(board), len(board[0])
        
        dist = {1: 0}
        queue = deque([1])
        while queue:
            cur = queue.popleft()
            if cur == m * n: return dist[cur]
            for k in range(cur + 1, min(cur + 7, m * n + 1)):
                i, j = self.convert_num_to_pos(m, n, k)
                #print(i, j, k)
                if board[i][j] != -1:
                    k = board[i][j]
                if k not in dist:
                    dist[k] = dist[cur] + 1
                    queue.append(k)
        return -1
    
    def convert_num_to_pos(self, m, n, num):
        i = m - 1 - (num - 1) // n
        j = (num - 1) % n
        if (m - 1 - i) % 2 == 1:
            j = n - 1 - j
        return (i, j)    
