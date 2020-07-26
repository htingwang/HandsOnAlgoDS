class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        for j in range(k + 1): dp[0][j] = 0
        #if k >= 1: dp[1][1] = 0
        for i in range(1, n + 1):
            for j in range(k + 1):
                same = diff = 0
                for l in range(i, n + 1):
                    if s[l - 1] == s[i - 1]: same += 1
                    else: diff += 1
                    if j + diff <= k:
                        if same >= 100: length = 4 #a123
                        elif same >= 10: length = 3 #a12
                        elif same >= 2: length = 2 #a3
                        else: length = 1 #a
                        #print(i, j, l, diff)
                        dp[l][j + diff] = min(dp[l][j + diff], dp[i - 1][j] + length)
                        if j + same+ diff <= k: dp[l][j + same+ diff] = min(dp[l][j + same+ diff], dp[i - 1][j])
        #print(dp)
        return dp[n][k]
