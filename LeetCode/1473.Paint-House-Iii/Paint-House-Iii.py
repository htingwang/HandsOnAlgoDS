class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        # houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
        dp = [[[float('inf')] * n for _ in range(target)] for __ in range(m)]
        
        if houses[0] != 0: dp[0][0][houses[0] - 1] = 0
        else:
            for k in range(n): dp[0][0][k] = cost[0][k]
                
        for i in range(1, m):
            for j in range(target):
                for k in (range(n) if houses[i] == 0 else [houses[i] - 1]):
                    for prek in range(n):    
                        if k == prek:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][prek] + (0 if houses[i] != 0 else cost[i][k]))
                        elif j > 0:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - 1][prek] + (0 if houses[i] != 0 else cost[i][k]))

        res = min(dp[m - 1][target - 1])
        if res == float('inf'): return -1
        return res
