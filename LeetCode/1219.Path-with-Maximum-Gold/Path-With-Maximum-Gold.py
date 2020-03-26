class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        row, col = len(grid), len(grid[0])
        self.res = 0
        seen = set()
        
        for i in range(row):
            for j in range(col):
                self.dfs(i, j, seen, row, col, grid, grid[i][j])
        return self.res
    
    def dfs(self, i, j, seen, row, col, grid, score):
        if not grid[i][j]:
            return
        seen.add((i, j))
        self.res = max(self.res, score)
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= ni < row and 0 <= nj < col and (ni, nj) not in seen:
                self.dfs(ni, nj, seen, row, col, grid, score + grid[ni][nj])
        seen.remove((i, j))
