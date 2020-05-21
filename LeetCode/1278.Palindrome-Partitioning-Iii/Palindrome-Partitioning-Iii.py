class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        for i in range(n):
            dp[i][1] = self.change(s[:i + 1])
            
        for i in range(n):    
            for j in range(2, k + 1):
                for l in range(min(i, n - 1)):
                    dp[i][j] = min(dp[i][j], dp[l][j - 1] + self.change(s[l + 1 : i + 1]))
                
        return dp[n - 1][k]
        
    def change(self, s):
        res = 0
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] != s[r]: res += 1
            l += 1
            r -= 1
        return res
        
