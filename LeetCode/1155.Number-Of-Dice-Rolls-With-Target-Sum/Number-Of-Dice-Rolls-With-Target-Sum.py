class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        mod = pow(10, 9) + 7
        nums = set(range(1, f + 1))
        #print(nums)
        dp = [[0] * (d + 1) for _ in range(target + 1)] 
        
        for i in range(1, min(f + 1, target + 1)):
            dp[i][1] = 1
                
        for i in range(1, target + 1):
            for j in range(2, d + 1):
                for k in range(1, f + 1):
                    if i >= k:
                        dp[i][j] += dp[i - k][j - 1]
        #print(dp)            
        return dp[target][d] % mod
