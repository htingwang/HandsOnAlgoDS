class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if len(s3) != m + n: return False
        
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(1, m + 1):
            f[i][0] = s1[:i] == s3[:i]
        for j in range(1, n + 1):
            f[0][j] = s2[:j] == s3[:j]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s3[i + j - 1]:
                    f[i][j] |= f[i - 1][j]
                if s2[j - 1] == s3[i + j - 1]:
                    f[i][j] |= f[i][j - 1]
        return f[m][n]
                
