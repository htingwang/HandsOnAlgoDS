class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        start = end = [-1, -1]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: start = [i, j]
                if grid[i][j] == 0: count += 1
                if grid[i][j] == 2: end = [i, j]
        return self.dfs(grid, start[0], start[1], count + 1)
    
    def dfs(self, grid, i, j, count):
        ans = 0
        if i < 0 or j < 0: return 0
        if i >= len(grid) or j >= len(grid[0]): return 0
        if 0 == count and grid[i][j] == 2: return 1
        if grid[i][j] == 2 or grid[i][j] == -1 : return 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            tmp, grid[i][j] = grid[i][j], -1
            ans += self.dfs(grid, i + dx, j + dy, count - 1)
            grid[i][j] = tmp
        return ans
