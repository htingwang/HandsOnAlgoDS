class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = [], []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: rows.append(i)
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1: cols.append(j)
        
        def dist(points):
            res = 0
            i, j = 0, len(points) - 1
            while i < j:
                res += points[j] - points[i]
                i += 1
                j -= 1
            return res
        
        return dist(rows) + dist(cols)
        
