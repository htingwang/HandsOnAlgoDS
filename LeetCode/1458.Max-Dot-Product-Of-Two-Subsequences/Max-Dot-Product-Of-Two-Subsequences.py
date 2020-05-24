class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)
        dp = [[nums1[i] * nums2[j] for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + max(0, nums1[i] * nums2[j]))
        return dp[m - 1][n - 1]
        
        
