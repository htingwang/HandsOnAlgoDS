class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        L = len(A);
        dp = [0] * L;
        for i in range(L):
            curMax = 0;
            for k in range(1, min(K, i+1)+1):
                curMax = max(curMax, A[i-k+1]);
                if i<k:
                    dp[i] = max(dp[i], k*curMax);
                else:
                    dp[i] = max(dp[i], dp[i-k]+k*curMax);
                #print [i, k, curMax, dp[i]]
        return dp[L-1];
