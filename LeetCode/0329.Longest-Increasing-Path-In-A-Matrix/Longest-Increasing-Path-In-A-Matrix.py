class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        res = 1
        
        def dfs(i, j):
            if memo[i][j]: return memo[i][j]
            
            res = 1
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] < matrix[i][j]:
                    res = max(res, 1 + dfs(ni, nj))
            
            memo[i][j] = res
            return res
        
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        
        return res
        
