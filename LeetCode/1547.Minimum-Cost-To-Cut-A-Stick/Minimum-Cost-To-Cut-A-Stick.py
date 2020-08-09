class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        cuts = [0] + sorted(cuts) + [n]
        dp = [[float('inf')] * 102 for _ in range(102)]
        for j in range(1, len(cuts)):
            for i in range(j - 1, -1, -1):
                if i + 1 < j:
                    for k in range(i + 1, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
                    dp[i][j] += cuts[j] - cuts[i]
                else:
                    dp[i][j] = cuts[j] - cuts[i]
        return dp[0][len(cuts) - 1] - n
                
