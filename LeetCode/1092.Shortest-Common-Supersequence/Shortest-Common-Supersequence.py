class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def findLCS(str1, n, str2, m):
            dp = [[""] * (m + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if str1[i - 1] == str2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key = len)
            return dp[n][m]
        n = len(str1)
        m = len(str2)
        lcs = findLCS(str1, n, str2, m)
        #print lcs
        ans = ""
        i = j = 0
        for c in lcs:
            #print c
            while str1[i] != c:
                ans += str1[i]
                i += 1
            while str2[j] != c:
                ans += str2[j]
                j += 1
            ans += c
            i += 1
            j += 1
        
        return ans + str1[i:] + str2[j:]
