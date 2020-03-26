class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2): return False
        if s1 == s2: return True
        if sorted(s1) != sorted(s2): return False
        
        n = len(s1)
        dp = [[[False] * (n + 1) for _ in range(n)] for __ in range(n)]
        
        for l in range(1, n + 1):
            for i in range(n):
                for j in range(n):
                    if l == 1:
                        dp[i][j][l] = s1[i] == s2[j]
                        continue
                    for k in range(1, l):
                        if i + l > n or j + l > n: continue
                        if dp[i][j][k] and dp[i + k][j + k][l - k]:
                            dp[i][j][l] = True
                            break
                        if dp[i][j + l - k][k] and dp[i + k][j][l - k]:
                            dp[i][j][l] = True
                            break
        return dp[0][0][n]     
