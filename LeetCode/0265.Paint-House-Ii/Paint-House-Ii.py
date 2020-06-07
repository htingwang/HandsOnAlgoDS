class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        n = len(costs)
        res = [(0, float('inf')), (0, float('inf'))]
        for color, cost in enumerate(costs[0]):
            if cost < res[0][1]:
                res[1] = res[0]
                res[0] = (color, cost)
            elif cost < res[1][1]:
                res[1] = (color, cost)
        for i in range(1, n):
            cur = [(0, float('inf')), (0, float('inf'))]
            for color, cost in enumerate(costs[i]):
                if color != res[0][0]:
                    ncost = cost + res[0][1]
                else:
                    ncost = cost + res[1][1]
                if ncost < cur[0][1]:
                    cur[1] = cur[0]
                    cur[0] = (color, ncost)
                elif ncost < cur[1][1]:
                    cur[1] = (color, ncost)
            res = list(cur)
            
        return res[0][1]
                
