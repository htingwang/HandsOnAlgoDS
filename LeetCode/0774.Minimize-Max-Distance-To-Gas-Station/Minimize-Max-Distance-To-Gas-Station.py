class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        left, right = 0, stations[-1] - stations[0]
        while left + 10e-6 < right:
            mid = (left + right) / 2.0
            if self.check(stations, mid) > K:
                left = mid
            else:
                right = mid 
        return right
    
    def check(self, stations, d):
        res = 0
        for i in range(0, len(stations) - 1):
            res += math.ceil((stations[i + 1] - stations[i]) / d) - 1
        #print(d, res)
        return res
        
