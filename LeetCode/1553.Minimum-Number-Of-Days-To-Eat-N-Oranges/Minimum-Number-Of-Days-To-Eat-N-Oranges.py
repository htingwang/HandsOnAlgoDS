class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        #return self.minDays1(n)
        memo = {0: 0, 1: 1}
        def dfs(n):
            if n in memo : return memo[n]
            memo[n] = 1 + min(n % 2 + dfs(n // 2), n % 3 + dfs(n // 3))
            return memo[n]
        #print(self.minDays1(n))
        return dfs(n)
                
    # time limit exceed
    def minDays1(self, n):
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = 1 + dp[i - 1]
            if i % 2 == 0:
                dp[i] = min(dp[i], 1 + dp[i / 2])
            if i % 3 == 0:
                dp[i] = min(dp[i], 1 + dp[i / 3])
        #print(dp)
        return dp[n]
        
