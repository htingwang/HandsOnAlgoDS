class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0
        
        res = 0
        if k >= n // 2:
            for i in range(n - 1):
                if prices[i + 1] > prices[i]:
                    res += prices[i + 1] - prices[i]
            return res
        
        dp = [[0] * n for _ in range(k + 1)]
        
        for i in range(1, k + 1):
            local = dp[i - 1][0] - prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + local)
                local = max(local, dp[i - 1][j] - prices[j])
                
        return dp[k][n - 1]
