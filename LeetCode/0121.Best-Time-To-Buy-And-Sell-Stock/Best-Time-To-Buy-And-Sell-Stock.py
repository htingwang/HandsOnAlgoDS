class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if not n: return 0
        mn = prices[0]
        res = 0
        for i in range(1, n):
            res = max(res, prices[i] - mn)
            mn = min(mn, prices[i])
        return max(0, res)
        
