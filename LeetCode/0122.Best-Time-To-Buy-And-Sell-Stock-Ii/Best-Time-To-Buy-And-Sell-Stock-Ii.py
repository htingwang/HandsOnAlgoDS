class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        mn = float('inf')
        for p in prices:
            if p > mn:
                res += p - mn
                mn = p
            else:
                mn = min(mn, p)
        return res
        
