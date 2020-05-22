class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        for i in range(n): dp[i][1] = self.count(s[: i + 1])
        for i in range(n):
            for m in range(min(i, n - 1)):
                pd = self.count(s[m + 1 : i + 1])
                for j in range(2, k + 1):
                    dp[i][j] = min(dp[i][j], dp[m][j - 1] + pd)
        return dp[n - 1][k]
    
    def count(self, s):
        res = 0
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]: res += 1
            l += 1
            r -= 1
        return res
