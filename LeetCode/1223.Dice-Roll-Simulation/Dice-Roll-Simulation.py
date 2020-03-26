class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        mod = 10 ** 9 + 7
        roll_len = len(rollMax)
        dp = [[0] * (len(rollMax) + 1) for _ in range(n + 1)]
        for i in range(roll_len):
            dp[1][i] = 1
        dp[0][roll_len] = 1
        dp[1][roll_len] = roll_len
        
        for i in range(2, n + 1):
            for j in range(roll_len):
                for k in range(1, i + 1):
                    if k > rollMax[j]: break
                    dp[i][j] += dp[i - k][roll_len] - dp[i - k][j]
                    dp[i][j] %= mod
                dp[i][roll_len] += dp[i][j]
                dp[i][roll_len] %= mod
        return dp[n][roll_len]
