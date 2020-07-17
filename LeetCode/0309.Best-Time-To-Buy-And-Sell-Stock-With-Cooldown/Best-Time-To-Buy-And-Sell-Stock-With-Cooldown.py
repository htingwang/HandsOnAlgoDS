class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0
        
        dp = [0] * n
        prev = -prices[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1], prices[i] + prev)
            prev = max(prev, dp[i - 2] - prices[i])
        return dp[-1]
        
