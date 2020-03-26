class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        edge = 0
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 if int(matrix[i][j]) else 0
                edge = max(edge, dp[i][j])
        return edge * edge
                
