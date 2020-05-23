class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        return self.slidingPuzzle2(board)
    
    # BFS. Time: O(R*C*(R*C)!). Space: O(R*C*(R*C)!)
    def slidingPuzzle1(self, board):
        m, n = len(board), len(board[0])
        target = tuple(range(1, m * n) + [0])
        target_wrong = tuple(range(1, m * n - 2) + [m * n - 1, m * n - 2, 0])
        start = []
        zero = 0
        for i in range(m):
            for j in range(n):
                start.append(board[i][j])
                if board[i][j] == 0: zero = i *n + j
        start = tuple(start)
        seen = {start}
        queue = collections.deque([(start, zero, 0)])
        
        while queue:
            cboard, zero, cost = queue.popleft()
            if cboard == target: return cost
            if cboard == target_wrong: return -1
            i, j = zero // n, zero % n
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n:
                    nei = ni * n + nj
                    nboard = list(cboard)
                    nboard[zero], nboard[nei] = nboard[nei], nboard[zero]
                    nboard = tuple(nboard)
                    if nboard not in seen:
                        seen.add(nboard)
                        queue.append((nboard, nei, cost + 1))
        
        return -1
        
    # A* algorithm. Time: O(R*C*(R*C)!). Space: O(R*C*(R*C)!)
    def slidingPuzzle2(self, board):
        m, n = len(board), len(board[0])
        expected = {(r * n + c + 1) % (m * n): (r, c) for r in range(m) for c in range(n)}

        def heuristic(board):
            res = 0
            for r in range(m):
                for c in range(n):
                    val = r * n + c
                    if board[val] == 0: continue
                    er, ec = expected[board[val]]
                    res += abs(r - er) + abs(c - ec)
            return res    
        
        start = []
        zero = 0
        for r in range(m):
            for c in range(n):
                start.append(board[r][c])
                if board[r][c] == 0: zero = r * n + c
        target = tuple(range(1, m * n) + [0])
        target_wrong = tuple(range(1, m * n - 2) + [m * n - 1, m * n - 2, 0])
        minheap = [(0, 0, tuple(start), zero)]
        ecosts = {tuple(start): 0}
        while minheap:
            ecost, cost, cboard, zero = heapq.heappop(minheap)
            if cboard == target: return cost
            if cboard == target_wrong: return -1
            if ecost > ecosts[cboard]: continue
                
            r, c = zero // n, zero % n
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n:
                    nei = nr * n + nc
                    nboard = list(cboard)
                    nboard[nei], nboard[zero] = nboard[zero], nboard[nei]
                    nboard = tuple(nboard)
                    necost = cost + 1 + heuristic(nboard)
                    if necost < ecosts.get(nboard, float('inf')):
                        ecosts[nboard] = necost
                        heapq.heappush(minheap, (necost, cost + 1, nboard, nei))
        return -1        
