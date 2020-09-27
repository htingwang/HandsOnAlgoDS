class Solution(object):
    def connectTwoGroups(self, cost):
        """
        :type cost: List[List[int]]
        :rtype: int
        """
        m, n = len(cost), len(cost[0])
        
        row = [float('inf')] * n
        for j in range(n):
            for i in range(m):
                row[j] = min(row[j], cost[i][j])
                
        dp = [[-1] * 4096 for _ in range(12)]
        
        def dfs(i, mask, m, n):
            res = 0
            if i == m:
                for j in range(n):
                    if (mask & (1 << j) == 0):
                        res += row[j]
            else:
                if dp[i][mask] != -1:
                    return dp[i][mask]
                res = float('inf')
                for j in range(n):
                    res = min(res, cost[i][j] + dfs(i + 1, mask | (1 << j), m, n))
                dp[i][mask] = res
            return res
        
        return dfs(0, 0, m, n)
