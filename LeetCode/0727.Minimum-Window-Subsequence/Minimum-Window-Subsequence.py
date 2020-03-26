class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # dp[i][j]: start index of S when S[:i] includes T[:j]
        start = -1
        l = float('inf')
        m, n = len(S), len(T)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1): dp[i][0] = i
        for i in range(1, m + 1):
            for j in range(1, min(i + 1, n + 1)):
                if S[i - 1] == T[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
            if dp[i][n] != -1:
                if i - dp[i][n] < l:
                    l = i - dp[i][n]
                    start = dp[i][n]
        #print(dp)
        return S[start : start + l] if start != -1 else ""
