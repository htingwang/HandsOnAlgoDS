class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        dp = [1] * n
        cnt = [1] * n
        res = 0
        max_len= 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 >= dp[i]:
                        if dp[j] + 1 == dp[i]: cnt[i] += cnt[j]
                        else: cnt[i] = cnt[j]
                        dp[i] = dp[j] + 1
            
            if dp[i] >= max_len:
                #print(i,dp[i], max_len, res, cnt)
                if dp[i] == max_len: res += cnt[i]
                else: res = cnt[i]
                max_len = dp[i]
        #print(dp)        
        return res
