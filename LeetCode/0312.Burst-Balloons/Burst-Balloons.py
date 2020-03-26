class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = [1] + nums + [1]
        n = len(nums)
        #print(nums)
        dp = [[0] * n for _ in range(n)]
        dp[0]
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        
        #print dp
        return dp[0][n - 1]
