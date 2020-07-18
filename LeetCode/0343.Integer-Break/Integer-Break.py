class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 1
        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1
        for i in range(3, n + 1):
            for j in range(2, i):
                if i - j <= 3: dp[i] = max(dp[i], j * (i - j))
                else: dp[i] = max(dp[i], j * dp[i - j], j * (i - j))
        return dp[n]
