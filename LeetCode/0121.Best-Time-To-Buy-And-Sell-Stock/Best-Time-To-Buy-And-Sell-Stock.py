class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profix = 0
        min_price = float('inf')
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profix:
                max_profix = prices[i] - min_price

        return max_profix
