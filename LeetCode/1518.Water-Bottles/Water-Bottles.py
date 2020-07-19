class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        res = numBottles
        while numBottles >= numExchange:
            res += numBottles // numExchange
            numBottles = numBottles - numExchange * (numBottles // numExchange) + numBottles // numExchange
        return res
        
