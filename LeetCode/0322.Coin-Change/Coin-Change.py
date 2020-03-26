class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        # import sys
        # python 2: sys.maxint, -sys.maxint - 1
        # python 3: sys.maxsize, -sys.maxsize - 1
        # float('inf'), float('-inf')
        dp[0] = 0
        for coin in coins:
            for i in range(1, amount + 1):
            
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
