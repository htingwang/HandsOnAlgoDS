class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[1] = [nums[0], 0]
        dp[2] = [nums[0], nums[1]]
        for i in range(3, n):
            dp[i][0] = max(nums[i - 1] + dp[i - 2][0], dp[i - 1][0])
            dp[i][1] = max(nums[i - 1] + dp[i - 2][1], dp[i - 1][1])
        #print(dp)
        return max(nums[-1] + dp[n - 2][1], dp[n - 1][0], dp[n - 1][1])
