class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2: return 0
        buy1 = buy2 = -sys.maxint - 1
        profit1 = profitall = 0
        for price in prices:
            profitall = max(profitall, buy2 + price)
            buy2 = max(buy2, profit1 - price)
            profit1 = max(profit1, price + buy1)
            buy1 = max(buy1, -price)
            
            
            
        return profitall
            
