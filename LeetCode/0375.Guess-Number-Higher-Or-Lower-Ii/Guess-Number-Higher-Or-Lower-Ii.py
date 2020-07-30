class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(i - 1, 0, -1):
                global_min = float('inf')
                for k in range(j + 1, i):
                    local_max = k + max(dp[j][k - 1], dp[k + 1][i])
                    global_min = min(global_min, local_max);
                dp[j][i] = j if j + 1 == i else global_min
        return dp[1][n]

