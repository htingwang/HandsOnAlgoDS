import heapq
class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        n = len(stones)
        if (n - 1) % (K - 1): return -1
        
        pre_sum = [0] * (n + 1)
        
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + stones[i - 1]
        
        dp = [[0] * n for _ in range(n)]
        
        for m in range(K, n + 1):
            for i in range(n - m + 1):
                j = i + m - 1
                dp[i][j] = float('inf')
                for mid in range(i, j, K - 1):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j])
                if (j - i) % (K - 1) == 0:
                    dp[i][j] += (pre_sum[j + 1] - pre_sum[i])
                    
        return dp[0][n - 1]
                    
