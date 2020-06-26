class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.canJump2(nums)
    
    def canJump1(self, nums):
        n = len(nums)
        dp = [0] * n
        for i in range(1, n):
            dp[i] = max(dp[i - 1], nums[i - 1]) - 1
            if dp[i] < 0: return False
        return True  
    
    def canJump2(self, nums):
        n = len(nums)
        reach = 0
        for i in range(n):
            if i > reach or reach >= n - 1: break
            reach = max(reach, i + nums[i])
        return reach >= n - 1
        
