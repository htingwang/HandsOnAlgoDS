class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        island = set()
        
        def dfs(i, j, di):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                shape.append(di)
                dfs(i + 1, j, 1)
                dfs(i - 1, j, 2)
                dfs(i, j + 1, 3)
                dfs(i, j - 1, 4)
                shape.append(0)
        
        for i in range(m):
            for j in range(n):
                shape = []
                dfs(i, j, 0)
                if shape: island.add(tuple(shape))
        return len(island)
