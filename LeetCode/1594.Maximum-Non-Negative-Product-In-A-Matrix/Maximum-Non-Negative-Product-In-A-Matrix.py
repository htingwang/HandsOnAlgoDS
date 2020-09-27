class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        mx = [[float('-inf')] * (n) for _ in range(m)]
        mn = [[float('inf')] * (n) for _ in range(m)]
        mod = 10 ** 9 + 7
        if grid[0][0] == 0: return 0
        mx[0][0] = mn[0][0] = grid[0][0]
        
        for i in range(1, m):
            mx[i][0] = max(grid[i][0] * mx[i - 1][0], grid[i][0] * mn[i - 1][0])
            mn[i][0] = min(grid[i][0] * mx[i - 1][0], grid[i][0] * mn[i - 1][0])
            
        for j in range(1, n):
            mx[0][j] = max(grid[0][j] * mx[0][j - 1], grid[0][j] * mn[0][j - 1])
            mn[0][j] = min(grid[0][j] * mx[0][j - 1], grid[0][j] * mn[0][j - 1])
            
        for i in range(1, m):
            for j in range(1, n):
                mx[i][j] = max(grid[i][j] * mx[i - 1][j], grid[i][j] * mx[i][j - 1], grid[i][j] * mn[i - 1][j], grid[i][j] * mn[i][j - 1])
                mn[i][j] = min(grid[i][j] * mx[i - 1][j], grid[i][j] * mx[i][j - 1], grid[i][j] * mn[i - 1][j], grid[i][j] * mn[i][j - 1])
        
        #print(mx)
        #print(mn)
        return mx[m - 1][n - 1] % mod if mx[m - 1][n - 1] >= 0 else -1
