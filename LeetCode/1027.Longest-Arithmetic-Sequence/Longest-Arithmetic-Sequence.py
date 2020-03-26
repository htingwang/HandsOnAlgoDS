class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        dp = [collections.defaultdict(int) for _ in range(len(A))]
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                dp[j][diff] = dp[i][diff] + 1
                res = max(res, dp[j][diff] + 1)
        return res
                
        
