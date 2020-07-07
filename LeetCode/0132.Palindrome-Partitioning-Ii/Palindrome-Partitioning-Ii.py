class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        p = [[False] * n for _ in range(n)]
        dp = [i for i in range(n)]
        
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i <= 2 or p[i + 1][j - 1]):
                    p[i][j] = True
                    dp[j] = 0 if i == 0 else min(dp[j], dp[i - 1] + 1)
                    
        return dp[n - 1]
        
