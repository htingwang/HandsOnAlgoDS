class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        n = len(startTime)
        info = sorted(zip(startTime, endTime, profit), key=lambda v: v[0])
        #print(info)
        startTime = [info[i][0] for i in range(n)]
        
        dp = [0] * (n + 1)
        dp[n - 1] = info[n - 1][2]
        for i in range(n - 2, -1, -1):
            j = bisect.bisect_left(startTime, info[i][1])
            dp[i] = max(dp[i + 1], dp[j] + info[i][2])
            
        #print(dp)
        return dp[0]
        
