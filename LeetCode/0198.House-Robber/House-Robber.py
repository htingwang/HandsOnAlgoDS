class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = nums[:]
        res = nums[0]
        for i in range(1, len(nums)):
            pre = 0
            if i > 1: pre = max(pre, dp[i - 2])
            if i > 2: pre = max(pre, dp[i - 3])
            dp[i] = nums[i] + pre
            res = max(res, dp[i])
        return res
