class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0;
        dp = [[0 for _ in range(len(s))] for __ in range(len(s))];
        #print dp
        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1;
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
        #print dp
        return dp[0][len(s) - 1]
        
