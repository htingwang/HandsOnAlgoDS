class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.numTrees1(n)
    
    def numTrees1(self, n):
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
    
    def numTrees2(self, n):
        res = 1
        for i in range(n):
            res = res * 2 * (2 * i + 1) / (i + 2)
        return res


