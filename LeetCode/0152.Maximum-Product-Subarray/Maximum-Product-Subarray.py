class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[num for num in nums] for _ in range(2)] 
        #print(dp)
        res = nums[0]
        for i in range(1, len(nums)):
            #print(i, dp[0][i - 1], dp[1][i - 1])
            dp[0][i] = max(nums[i], nums[i] * dp[0][i - 1], nums[i] * dp[1][i - 1])
            dp[1][i] = min(nums[i], nums[i] * dp[0][i - 1], nums[i] * dp[1][i - 1])
            res = max(res, dp[0][i])
        #print(dp)
        return res
        
