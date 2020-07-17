class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = float('inf')
        m, n = len(grid), len(grid[0])
        empty = 0
        dist = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = float('inf')
                    queue = collections.deque()
                    queue.append((0, i, j))
                    while queue:
                        d, x, y = queue.popleft()
                        for nx, ny in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == empty:
                                grid[nx][ny] -= 1
                                dist[nx][ny] += d + 1
                                res = min(res, dist[nx][ny])
                                queue.append((d + 1, nx, ny))
                    empty -= 1
        return -1 if res == float('inf') else res
