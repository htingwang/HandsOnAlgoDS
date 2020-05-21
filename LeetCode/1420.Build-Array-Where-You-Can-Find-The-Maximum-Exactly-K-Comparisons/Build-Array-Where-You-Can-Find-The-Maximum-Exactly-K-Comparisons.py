class Solution(object):
    def numOfArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]
        for i in range(m + 1): dp[0][i][0] = 1
            
        for i in range(1, n + 1):
              for j in range(1, m + 1):
                    for a in range(1, k + 1):
                        # all i numbers does not contain j
                        dp[i][j][a] += dp[i][j - 1][a] % mod
                        # i-1 numbers does not contain j, ith number is j
                        dp[i][j][a] += dp[i - 1][j - 1][a - 1] % mod
                        # i-1 numbers contain j
                        dp[i][j][a] += ((dp[i - 1][j][a] - dp[i - 1][j - 1][a]) * j) % mod
                        
        return dp[n][m][k] % mod
