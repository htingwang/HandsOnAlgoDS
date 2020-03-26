class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0: return 0;
        ans = 0;
        for i in range(1, len(timeSeries)):
            if timeSeries[i]-timeSeries[i-1] < duration:
                ans += (timeSeries[i]-timeSeries[i-1]);
            else:
                ans += duration;
        return ans + duration;
        
